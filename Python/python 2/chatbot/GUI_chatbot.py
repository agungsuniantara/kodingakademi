import pickle
import numpy as np
import json
import random
from tkinter import *
from keras.models import load_model
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

model = load_model('chatbot\chatbot_model.h5')
intents = json.loads(open('chatbot\dataset.json').read())
words = pickle.load(open('chatbot\words.pkl','rb'))
classes = pickle.load(open('chatbot\classes.pkl','rb'))

factory = StemmerFactory()
stemmer = factory.create_stemmer()

def clean_up_sentence(sentence):
    #tokenisasi pattern - memisahkan kata menjadi array
    sentence_words = sentence.split()
    #stemming setiap kata - mengubah menjadi kata dasar
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

#return array bag of words : 0 atau 1 untuk kata yang ada dalam kalimat
def bag_of_words(sentence, words, show_details=True):
    #tokenisasi patterns
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words) 
    for s in sentence_words:
        for i,word in enumerate(words):
            if word == s: 
                #tetapkan nilai 1 jika kata ini berada di kosakata
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % word)
                    
    return(np.array(bag))

def predict_class(sentence, hargaMax=None, kota=None):
    #memfilter prediksi dibawah ambang batas
    p = bag_of_words(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]

    #sorting strength probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list=[]
    
    if kota == []:
        kota = None

    #Jika tidak ada yang digunakan sebagai filter
    if hargaMax is None and kota is None:
        for r in results:
            return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    
        if not return_list:
            return_list.append({"intent": "salah", "probability": "1.0"})
    
    #Jika kota tidak digunakan sebagai filter
    elif kota is None:
        for r in results:
            if classes[r[0]] not in ["salah", "sapaan", "selesai", "terimakasih"]:
                return_list.append({"intent": classes[r[0]], "probability": str(r[1]), "harga": hargaMax})
            else:
                return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    
        if not return_list:
            return_list.append({"intent": "salah", "probability": "1.0"})
    
    #jika harga tidak digunakan sebagai filter
    elif hargaMax is None:
        for r in results:
            if classes[r[0]] not in ["salah", "sapaan", "selesai", "terimakasih"]:
                return_list.append({"intent": classes[r[0]], "probability": str(r[1]), "kota": kota})
            else:
                return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    
        if not return_list:
            return_list.append({"intent": "salah", "probability": "1.0"})
    
    #Jika kota dan harga digunakan sebagai filter
    else:
        for r in results:
            if classes[r[0]] not in ["salah", "sapaan", "selesai", "terimakasih"]:
                return_list.append({"intent": classes[r[0]], "probability": str(r[1]), "kota": kota, "harga": hargaMax})
            else:
                return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    
        if not return_list:
            return_list.append({"intent": "salah", "probability": "1.0"})

    print(return_list)
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    
    try:
        harga_max = ints[0]['harga']
    except KeyError:
        harga_max = None

    try:
        kota_inp = ints[0]['kota']
    except KeyError:
        kota_inp = None

    list_of_intents = intents_json['intents']

#jika tag adalah salah satu diantara sapaan, selesai, atau terimakasih
    if tag in ["sapaan", "selesai", "terimakasih"]:
        for i in list_of_intents:
            if(i['tag']== tag):
                result = random.choice(i['responses'])
                break
        return result
#jika tag selain itu
    else:
        all_responses = []
        for i in list_of_intents:
            if i['tag'] == tag:
                #Jika kota dan harga digunakan sebagai filter
                if kota_inp is not None and 'kota' in i and harga_max is not None and 'harga' in i:
                    for response, kota, harga in zip(i['responses'], i['kota'], i['harga']):
                        if kota.lower() == kota_inp.lower() and harga <= harga_max and response not in all_responses:
                            all_responses.append(response)
                    if not all_responses:
                        return "Tidak ada tempat yang sesuai dengan kota dan harga yang kamu inginkan"
                    return "\n".join(all_responses)
                
                #Jika hanya kota yang digunakan sebagai filter, harga tidak
                elif kota_inp is not None and 'kota' in i:
                    for response, kota in zip(i['responses'], i['kota']):
                        if kota.lower() == kota_inp.lower() and response not in all_responses:
                            all_responses.append(response)
                    if not all_responses:
                        return "Tidak ada tempat yang sesuai dengan kota yang kamu inginkan"
                    return "\n".join(all_responses)
                
                #Jika hanya harga yang digunakan sebagai filter, kota tidak
                elif harga_max is not None and 'harga' in i:
                    for response, harga in zip(i['responses'], i['harga']):
                        if harga <= harga_max and response not in all_responses:
                            all_responses.append(response)
                    if not all_responses:
                        return "Tidak ada tempat yang sesuai dengan harga yang kamu inginkan"
                    return "\n".join(all_responses)
                
                #Jika tidak ada yang digunakan sebagai filter
                else:
                    if 'responses' in i:
                        all_responses += i['responses']
                    return "\n".join(all_responses)

def show_filter_kota():
    hasil = [kota for kota, value in {
        "Badung": kota1.get(),
        "Bangli": kota2.get(),
        "Buleleng": kota3.get(),
        "Denpasar": kota4.get(),
        "Gianyar": kota5.get(),
        "Jembrana": kota6.get(),
        "Karangasem": kota7.get(),
        "Klungkung": kota8.get(),
        "Tabanan": kota9.get(),
    }.items() if value == 1]

    if len(hasil) == 9:
        hasil_check = "Seluruh Bali"
    else:
        hasil_check = ", ".join(hasil)
    k.config(text="Daerah\t: " + hasil_check)

    return hasil_check

def show_filter_harga():
    hasil_slide = str(harga.get())
    h.config(text="Harga max : " + hasil_slide)

    return hasil_slide

def extract_kota(sentence):
    kota_list = ["Badung", "Bangli", "Buleleng", "Denpasar", "Gianyar", "Jembrana", "Karangasem", "Klungkung", "Tabanan"]
    kota_input = []
    for kota in kota_list:
        if kota.lower() in sentence.lower():
            kota_input.append(kota)

    print(kota_input)
    return kota_input

def cari():
    hasil_check = show_filter_kota()
    hasil_slide = show_filter_harga()

    msg = entry.get("1.0",'end-1c').strip()

#jika tidak ada filter yang digunakan
    if len(hasil_check) == 0 and hasil_slide == "0":
        tampil_msg = entry.get("1.0",'end-1c').strip()

#jika hanya ada filter harga, tidak ada kota
    elif len(hasil_check) == 0:
        tampil_msg = entry.get("1.0",'end-1c').strip() + " dengan harga masuk maksimal " + hasil_slide

#jika hanya ada filter kota, tidak ada harga
    elif hasil_slide == "0":
         tampil_msg = entry.get("1.0",'end-1c').strip() + " di " + hasil_check

#jika kedua filter digunakan
    else:
        tampil_msg = entry.get("1.0",'end-1c').strip() + " di " + hasil_check + " dengan harga masuk maksimal " + hasil_slide

    if msg != '':
        mylist.config(state=NORMAL)
        mylist.insert(END, "You : " + tampil_msg + '\n\n')
        mylist.config()

        mylist.insert(END, "Bot : ")

#memproses filter kota
        kota_input = None
        if len(hasil_check) == 0:
            kota_input = extract_kota(msg)
        else:
            kota_input = extract_kota(hasil_check)
        jum_kota = len(kota_input)

#memproses filter harga
        harga = None
        if hasil_slide != "0":
            harga = int(hasil_slide)

#jika list kota tidak kosong
        if jum_kota != 0:
            for i in range(jum_kota):
                print(kota_input[i])
                ints= predict_class(msg, harga, kota_input[i])
                res = getResponse(ints, intents)
                mylist.insert(END, res + '\n')
            mylist.insert(END, '\n') 

#jika list kota kosong
        else:
            ints= predict_class(msg, harga, kota_input)
            res = getResponse(ints, intents)
            mylist.insert(END, res + '\n\n')

        mylist.config(state=DISABLED)
        mylist.yview(END)

#membuat GUI dengan tkinter

root = Tk()
root.geometry("1000x600")
root.title("Chatbot")

welcome = "Selamat Datang!\nKami akan berikan rekomendasi destinasi wisata di Bali\nsesuai dengan keinginanmu\n"

lf = LabelFrame(root, text=welcome, labelanchor=N)
lf.grid(row=0, column=0, rowspan=3, padx=10, sticky=NSEW)

kota1 = IntVar()
kota2 = IntVar()
kota3 = IntVar()
kota4 = IntVar()
kota5 = IntVar()
kota6 = IntVar()
kota7 = IntVar()
kota8 = IntVar()
kota9 = IntVar()

lf1 = LabelFrame(lf, text="Filter Kota")
lf1.grid(row=1, column=0, padx=5, rowspan=6, columnspan=2, sticky=NSEW)

opsi1 = Checkbutton(lf1, text='Badung', variable=kota1)
opsi1.grid(row=2, column=0, sticky=W)

opsi2 = Checkbutton(lf1, text='Bangli', variable=kota2)
opsi2.grid(row=2, column=1, sticky=W)

opsi3 = Checkbutton(lf1, text='Buleleng', variable=kota3)
opsi3.grid(row=3, column=0, sticky=W)

opsi4 = Checkbutton(lf1, text='Denpasar', variable=kota4)
opsi4.grid(row=3, column=1, sticky=W)

opsi5 = Checkbutton(lf1, text='Gianyar', variable=kota5)
opsi5.grid(row=4, column=0, sticky=W)

opsi6 = Checkbutton(lf1, text='Jembrana', variable=kota6)
opsi6.grid(row=4, column=1, sticky=W)

opsi7 = Checkbutton(lf1,text='Karangasem',variable=kota7)
opsi7.grid(row=5, column=0, sticky=W)

opsi8 = Checkbutton(lf1,text='Klungkung',variable=kota8)
opsi8.grid(row=5, column=1, sticky=W)

opsi9 = Checkbutton(lf1, text='Tabanan', variable=kota9)
opsi9.grid(row=6, column=0, sticky=W)

proses_kota = Button(lf, text='Terapkan', command=show_filter_kota)
proses_kota.grid(row=7, column=0, padx=75, sticky=W)

lf2 = LabelFrame(lf, text="Filter Harga")
lf2.grid(row=8, column=0, padx=5, rowspan=5, pady=10)

harga = IntVar()

scale = Scale(lf2, variable=harga, from_=0, to=100000, resolution=1000, orient=HORIZONTAL, length=200)
scale.grid(row=9, column=0)

proses_harga = Button(lf, text='Terapkan', command=show_filter_harga)
proses_harga.grid(row=13, column=0, padx=75, sticky=W)

lf3 = LabelFrame(lf, text="Pencarian")
lf3.grid(row=1, column=2, padx=5, rowspan=3, columnspan=2, sticky=NSEW)

entry = Text(lf3, width=83, height=3, wrap=WORD)
entry.grid(row=2, column=2, padx=2)

button = Button(lf3, text="Cari", width=8, command=cari)
button.grid(row=2, column=3, padx=5)

lf4 = LabelFrame(lf)
lf4.grid(row=7, column=2, rowspan=20, padx=5, pady=10, sticky=SW)

scroll_bar = Scrollbar(lf4)
scroll_bar.pack(side = RIGHT, fill=Y)

mylist = Text(lf4, yscrollcommand = scroll_bar.set, width=90, height=20, wrap=WORD)
mylist.config(state=DISABLED)
mylist.pack()

scroll_bar.config(command = mylist.yview )

lf5 = LabelFrame(lf, text="Filter yang diterapkan")
lf5.grid(row=4, column=2, rowspan=3, padx=5, pady=5, sticky=NW)

k = Label(lf5, text="Daerah\t: ")
k.grid(row=5, column=2, padx=2, sticky=NW)

h = Label(lf5, text="Harga max : ")
h.grid(row=6, column=2, padx=2, sticky=NW)

root.mainloop()