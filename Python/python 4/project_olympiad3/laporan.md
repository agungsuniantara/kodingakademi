# EcoRescue — Presentation Guide

This guide is for presenters explaining the **EcoRescue** project to students or general audiences. Each section contains a brief explanation followed by technical details for talking points.

---

## 1. Project Overview

**EcoRescue** is a web-based conservation analysis platform that evaluates Fauna (Animalia), Flora (Plantae), Fungi (Fungi), and Chromista (Chromista) status using IUCN Red List v3.1 data. Built for the ICO 2026 Python category competition.

**Problem addressed:** Overexploitation — excessive harvesting of species (hunting, trading, logging) driving extinction.

**Key approach:** Anti-hallucination. All displayed numbers are traceable to IUCN guidelines. Components lacking quantitative basis in the guidelines are intentionally not modeled.

### Tech Stack
| Component | Library | Reason |
|-----------|---------|--------|
| UI & Routing | Streamlit | Fast prototyping, interactive widgets |
| Numerical Computing | NumPy | Population projection, array operations |
| Visualization | Matplotlib | Pie chart, bar chart, projection curves |
| Data Parsing | csv (stdlib) | No pandas, per competition rules |

**Competition constraints:**
- No pandas, scikit-learn, or other heavy ML/dataframe libraries.
- No external database. Data loaded from CSV to in-memory list of dicts.
- Runs fully offline.

---

## 2. Application Architecture

Single file `app.py` with 6 navigation pages in the sidebar:

```
app.py
├── Load Data (CSV → list[dict], cached)
├── Search Engine (exact-match + partial-match)
├── Analytics Engine (population projection + risk score)
├── Visualization (matplotlib figures)
└── UI Pages (Streamlit)
    ├── Species & Database
    ├── Conservation Dashboard
    ├── Extinction Predictor
    ├── Conservation Support
    ├── Education Quiz
    └── About & Impact
```

**Data flow:**
1. On startup, `load_database()` reads CSV into `list[dict]`.
2. Data is cached by Streamlit (`@st.cache_data`) to avoid reloading.
3. Each page calls analytics/visualization functions that work on in-memory data.

---

## 3. Features and Page Explanations

### 3.1 Species & Database

**Search Database tab:**
- Search species from CSV by common or scientific name.
- **Exact-match priority** — exact name matches appear first.
- Filters: organism group (All, Fauna, Flora, Fungi, Chromista), IUCN Status.

### 3.2 Conservation Dashboard

**What's displayed:**
- 4 summary metrics: total species, CR, EN, VU counts.
- Progress bar: percentage of threatened species.
- Pie chart: overall conservation status distribution.
- Bar chart: species count by threat level (CR, EN, VU, NT).
- Composition by Kingdom (ANIMALIA, PLANTAE, FUNGI, CHROMISTA).

**How to explain:**
> "This dashboard gives a quick overview of biodiversity status in the database. Like a weather dashboard, but for extinction risk."

### 3.3 Extinction Predictor

**Mathematical model:**

```
P(t) = P₀ × (1 + r)^t
```

- `P₀` from **Criterion C** (max mature individuals) via `_get_pop0()`
- `r` from **Criterion A2** via `_get_decay()`: `r = (1 − A2/100)^(1/horizon) − 1`
- `t` = time in years (CR: 10, EN: 20, VU: 100, others: 20 — per `IUCN_PROJECTION_YEARS`)
- Result clipped to 0 (population cannot be negative)

**Conservation Risk Score (0–100):**

```
Score = (Criterion E Probability × 0.85) + (Decline Fraction × 100 × 0.15)
```

- Criterion E probabilities: CR=50%, EN=20%, VU=10%, NT=5%, LC=1%, DD=15%, EX=100%, EW=95%
- Decline fraction = `1 - (final_population / initial_population)`

**Priority labels:**
- CRITICAL: score ≥ 80 (red)
- HIGH: score ≥ 60 (orange)
- MEDIUM: score ≥ 40 (yellow)
- LOW: score < 40 (green)

**Why no recovery curve:**
> "IUCN assesses risk assuming 'no conservation action'. There are no official numbers for how effective each intervention (anti-poaching, captive breeding, etc.) is at slowing decline. Displaying unsourced numbers would be misleading."

**How to explain to students:**
> "Pick a species, then look at the graph. The red line shows how long the species lasts with no action taken. The steeper the drop, the more critical the situation."

### 3.4 Conservation Support

**Purpose:** Connect identified high-risk species with actionable conservation organizations and programs.

**What's displayed:**
- Filter by organism group: All, Fauna, Flora, Fungi, Chromista.
- Summary metrics: CR, EN, VU counts from the database.
- 9 conservation organizations with name, type, focus, description, key actions, and website links.
- Organizations filtered by kingdom relevance (e.g., Fauna filter shows only fauna-focused orgs).
- "How You Can Help" guide with 6 actionable steps.

**Conservation organizations included:**
| Organization | Type | Focus |
|---|---|---|
| IUCN SSC | Global Authority | All threatened species |
| WWF | NGO Global | Tiger, Rhino, Elephant, Orangutan |
| ZSL | Captive Breeding & Research | Tiger, Penguin, Amphibians |
| BGCI | Global Authority | Threatened plants |
| Missouri Botanical Garden | Captive Breeding & Research | Tropical plants, Orchids |
| TRAFFIC | Anti-Trafficking | All exploited species |
| Global Wildlife Conservation | Captive Breeding & Habitat | Critically Endangered species |
| Coral Triangle Initiative | Habitat Restoration | Marine species, Coral |
| Rainforest Alliance | Habitat Restoration | Tropical flora & fauna |

**How to explain:**
> "After we identify which species are at risk, the next question is: who is already doing something about it? This page connects the data to real organizations working on the ground."

### 3.5 Education Quiz

- 4 multiple-choice questions on overexploitation and IUCN.
- Score calculated as percentage of correct answers (0–100).
- Badges: CONSERVATION EXPERT (100), NATURE GUARDIAN (≥50), CARING BEGINNER (<50).
- State management via `st.session_state`.

### 3.6 About & Impact

- Explanation of the overexploitation problem.
- Summary of the 5 application features.
- Real-world actions students can take.

---

## 4. Scientific Methods Used

### 4.1 IUCN_PROFILES Data Structure

The data structure replicates Criteria A, C, D, and E separately, per IUCN documentation:

```python
IUCN_PROFILES = {
    "CR": {
        "label": "Critically Endangered",
        "kriteria_A_penurunan_populasi_persen": {"A1": 90, "A2_A4": 80},
        "kriteria_C_maks_individu_dewasa": 250,
        "kriteria_D_maks_individu_dewasa": 50,
        "kriteria_E_probabilitas_punah_persen": 50,
        "kriteria_E_rentang_waktu": "10 years or 3 generations",
        "ui_color": "#dc2626",
    },
    # ... EN, VU, NT, LC, DD, EX, EW
}
```

NT, LC, DD, EX, EW categories only have `deskripsi` (no explicit quantitative IUCN thresholds). Fallbacks are taken via `_get_pop0()`, `_get_decay()`, `_get_e_prob()`.

### 4.2 Derived Numbers from IUCN Criteria

| Category | P₀ (from Criterion C/D) | r (from Criterion A2) | Probability (Criterion E) |
|----------|------------------------|----------------------|---------------------------|
| CR | 250 | −14.87%/year (10 yr) | 50% (10 yr / 3 generations) |
| EN | 2,500 | −3.41%/year (20 yr) | 20% (20 yr / 5 generations) |
| VU | 10,000 | −0.36%/year (100 yr) | 10% (100 years) |
| NT | Estimate | Estimate | 5% |
| LC | Estimate | 0.00% | 1% |
| DD | Estimate | Estimate | 15% |
| EX | 0 | — | 100% |
| EW | 1 | — | 95% |

**r derivation from Criterion A2:**

General formula: `r = (1 - decline_fraction)^(1/horizon) - 1`

Horizon per category: CR=10 yr, EN=20 yr, VU=100 yr (from `IUCN_PROJECTION_YEARS`).

Example CR (80% decline, 10 yr): `r = (0.2)^(1/10) - 1 = -0.1487` → −14.87%/year
Example EN (50% decline, 20 yr): `r = (0.5)^(1/20) - 1 = -0.0341` → −3.41%/year
Example VU (30% decline, 100 yr): `r = (0.7)^(1/100) - 1 = -0.0036` → −0.36%/year

**Helper functions:**
- `_get_pop0(cat)` — retrieves P₀ from Criterion C (max mature individuals).
- `_get_decay(cat)` — computes r from Criterion A2.
- `_get_e_prob(cat)` — retrieves extinction probability from Criterion E.

### 4.3 Population Projection Model

Uses discrete exponential decay:

```
P(t) = P₀ × (1 + r)^t
```

- `P₀` from `_get_pop0()` (derived from Criterion C)
- `r` from `_get_decay()` (derived from Criterion A2)
- `t` = time in years (varies by category: CR=10, EN=20, VU=100, others=20)
- `np.clip(P, 0, None)` ensures non-negative population

### 4.4 Risk Score Calculation

```python
e_prob = _get_e_prob(category)        # Criterion E
decline_frac = 1 - (P_final / P_init) # from projection
score = e_prob * 0.85 + decline_frac * 100 * 0.15
```

- 85% weight from **Criterion E** (IUCN extinction probability).
- 15% weight from projected decline magnitude (numerical data).

---

## 5. File Structure

```
project_olympiad3/
├── app.py                  ← Full application
├── README.md               ← Technical documentation
├── extinction_predictor.md ← Extinction Predictor documentation
├── laporan.md              ← This presentation guide
├── guideline_iucn.pdf      ← IUCN Red List Categories and Criteria v3.1
├── data.csv                ← IUCN database (main data)
└── data.xlsx               ← IUCN database (Excel source)
```

---

## 6. Step-by-Step Demo Guide

### Setup
```bash
pip install streamlit numpy matplotlib
streamlit run app.py
```

### Demo 1: Search Species
1. Go to **Species & Database** tab.
2. Select **🐾 Fauna**.
3. Type "Tiger" in the search field.
4. Click the search result → see Risk Score and IUCN status.

### Demo 2: Extinction Predictor
1. Go to **Extinction Predictor** tab.
2. Select a species from the dropdown (e.g., komodo, tiger, rhino).
3. View the projection curve → explain that the red line = population with no action.

### Demo 3: Conservation Support
1. Go to **Conservation Support** tab.
2. Select **🐾 Fauna** to filter organizations.
3. Browse the listed organizations and their key actions.
4. Click "Visit Website" to see real conservation programs.

### Demo 4: Quiz
1. Go to **Education Quiz** tab.
2. Answer 4 questions.
3. View score and badge.

---

## 7. Key Points for Q&A

**Q: Why is there no recovery curve?**
> "IUCN assesses risk assuming no conservation action. There are no official numbers for intervention effectiveness. Adding a recovery curve would mean adding unsourced assumptions."

**Q: Where does the data come from?**
> "From the IUCN Red List, loaded into CSV. The app does not fetch data from the internet."

**Q: How long is the projection?**
> "It depends on the IUCN category. CR uses 10 years, EN uses 20 years, VU uses 100 years — matching the IUCN criteria timeframes. Other categories default to 20 years."

**Q: Does this work for all species?**
> "Yes, the model applies universally across all kingdoms — Animalia, Plantae, Fungi, and Chromista — because IUCN uses the same criteria for all taxonomic groups."

**Q: What conservation organizations are included?**
> "We list 9 real organizations covering captive breeding, habitat restoration, anti-trafficking, and research — each mapped to the kingdoms they serve."

---

## 8. Glossary

| Term | Brief Explanation |
|------|-------------------|
| IUCN | International Union for Conservation of Nature — global organization assessing species status |
| Red List | Global species conservation status list |
| Overexploitation | Harvesting species faster than they can regenerate |
| P₀ | Initial population — number of mature individuals at projection start |
| r | Annual population decline rate (negative = declining) |
| Risk Score | Risk score 0–100 combining IUCN category + projection |
| Exact-match | Exact name matching (name must be identical) |
| Heuristic | Rule-based approximation method, not ML |
