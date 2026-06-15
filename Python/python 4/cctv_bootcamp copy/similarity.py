import json
import numpy as np

def load_known_encodings(file_path):
    """Load known face encodings from JSONL file."""
    encodings = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line.strip())
            encodings.append({
                'name': data['name'],
                'encoding': np.array(data['encoding'])
            })
    return encodings

def load_detection_data(file_path):
    """Load detection data from JSONL file."""
    detections = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line.strip())
            detections.append({
                'classes': data.get('classes', []),
                'person_encodings': [np.array(enc) for enc in data.get('person_encodings', [])],
                'timestamp': data.get('timestamp', 0)
            })
    return detections

def find_best_match(person_encoding, known_encodings, threshold=0.6):
    """Find the best matching known face for a person encoding."""
    best_match = None
    best_similarity = -1

    person_norm = person_encoding / np.linalg.norm(person_encoding)

    for known in known_encodings:
        known_norm = known['encoding'] / np.linalg.norm(known['encoding'])
        similarity = np.dot(person_norm, known_norm)

        if similarity > best_similarity:
            best_similarity = similarity
            best_match = known['name']

    if best_similarity >= threshold:
        return best_match, best_similarity
    else:
        return "Unknown", best_similarity


known_encodings = load_known_encodings('face_encodings.jsonl')
detections = load_detection_data('detection_output.jsonl')

if not detections:
    print("No detection data found")

all_combined_results = []
for detection in detections:
    combined_results = []
    matched_persons = []

    for i, person_encoding in enumerate(detection['person_encodings']):
        match_name, similarity = find_best_match(person_encoding, known_encodings)
        combined_results.append({
            'person_id': i + 1,
            'matched_name': match_name,
            'similarity': similarity,
            'classes': detection['classes'], 
            'timestamp': detection['timestamp']
        })
        matched_persons.append(match_name)

    all_combined_results.extend(combined_results)


print("\n=== SUMMARY OF ALL DETECTIONS ===")

matched_person_data = {}
for result in all_combined_results:
    name = result['matched_name']
    if name != "Unknown":
        if name not in matched_person_data:
            matched_person_data[name] = {'classes': set(), 'timestamps': [], 'similarities': []}
        matched_person_data[name]['classes'].update(result['classes'])
        matched_person_data[name]['timestamps'].append(result['timestamp'])

for name, data in matched_person_data.items():
    print(f"Matched Person: {name}")
    print(f"Detected Classes: {list(data['classes'])}")
    print(f"Timestamps: {data['timestamps']}")
    print("---")
