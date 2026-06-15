import tkinter as tk
from tkinter import ttk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

KNOWLEDGE_BASE = {
  "how do motor vehicles cause carbon emissions": "Motor vehicles burn fossil fuels (gasoline/diesel), releasing exhaust gases such as carbon dioxide (CO2) and other greenhouse gases that contribute to global warming.",
  "what is the contribution of the transport sector to national emissions": "In Indonesia, the transport sector is one of the largest contributors to carbon emissions. According to data, its contribution can reach around 20–25% of total national emissions, mainly from private vehicles.",
  "how can I reduce the carbon footprint of my travel": "To reduce your travel carbon footprint, consider switching to public transportation (bus, train), cycling, walking, or using electric/hybrid vehicles when possible. Combining trips and driving efficiently also helps.",
  "what happens if I switch from a motorcycle to public transport for a year": "If you switch from a motorcycle to public transportation for a year, you can significantly reduce CO2 emissions, save fuel costs, reduce congestion, and contribute to cleaner air. The emission reduction can reach hundreds of kilograms of CO2 per year depending on travel distance.",
  "what is carbon emission": "Carbon emission is the release of carbon gases into the Earth's atmosphere, mainly carbon dioxide (CO2), mostly produced by fossil fuel combustion due to human activity and is a major cause of climate change.",
  "what are the impacts of carbon emissions on the environment": "The impacts of carbon emissions include global warming, extreme climate events (floods, droughts), rising sea levels, damage to marine ecosystems (coral bleaching), and health problems due to air pollution.",
  "sustainable transport tips": "Sustainable transport tips include: use public transportation, cycle or walk for short distances, consider electric vehicles, use carpooling, and maintain your vehicle for better fuel efficiency.",
  "definition of climate change": "Climate change refers to significant and long-term shifts in global or regional weather patterns, mainly caused by increased greenhouse gas concentrations in the atmosphere due to human activity.",
  "what are the main sources of carbon emissions": "The main sources of carbon emissions include fossil fuel combustion for electricity and transportation, deforestation, industrial activities, and intensive agriculture that produces methane (CH4) and nitrous oxide (N2O).",
  "how does deforestation relate to carbon emissions": "Deforestation reduces the Earth’s ability to absorb carbon dioxide due to fewer trees. In addition, the cutting and burning of forests release the carbon stored in the biomass of trees into the atmosphere.",
  "how can renewable energy reduce carbon emissions": "Renewable energy such as solar, wind, hydro, and biomass can produce electricity without burning fossil fuels. Replacing fossil-based sources with renewables drastically reduces CO2 emissions.",
  "what is the impact of carbon emissions on human health": "Carbon emissions are often accompanied by pollutants such as particulates (PM2.5) and nitrogen oxides that can cause respiratory issues, heart disease, and worsen chronic conditions like asthma.",
  "what is carbon footprint": "A carbon footprint is the total amount of greenhouse gases emitted directly or indirectly by an individual, organization, or product, usually expressed in kilograms or tons of CO2 equivalent.",
  "how to calculate personal carbon footprint": "A personal carbon footprint is calculated based on daily activities such as vehicle usage, electricity consumption, diet, and air travel. Many online calculators can estimate your total emissions based on this data.",
  "what is carbon neutrality": "Carbon neutrality means that the amount of carbon emitted equals the amount absorbed through actions like reforestation, energy efficiency, or carbon offsetting.",
  "examples of carbon reduction policies": "Examples of carbon reduction policies include carbon taxes, emission trading (carbon trading), renewable energy subsidies, and bans on forest burning.",
  "what is the role of individuals in reducing carbon emissions": "Individuals play a key role by adopting sustainable lifestyles such as saving energy, choosing eco-friendly transport, reducing meat consumption, and supporting environmentally responsible companies.",
  "difference between CO2 and other greenhouse gases": "CO2 is the most common greenhouse gas from fuel combustion. However, there are others like methane (CH4), nitrous oxide (N2O), and fluorinated gases that have stronger warming effects even in smaller amounts.",
  "how does industry contribute to carbon emissions": "The industrial sector emits carbon through production processes, fossil fuel energy use in machinery, and chemical reactions (such as cement and steel production) that release CO2 into the atmosphere.",
  "what is the relationship between electricity use and carbon emissions": "Most electricity in Indonesia is still generated from coal or gas power plants. The higher the electricity use, the larger the carbon emissions if the energy source is not renewable.",
  "what is carbon capture": "Carbon Capture, Utilization, and Storage (CCUS) is a technology that captures CO2 from major emission sources (like power plants and factories), then permanently stores it underground or repurposes it for other uses.",
  "how does agriculture contribute to carbon emissions": "Agriculture contributes to emissions through the use of nitrogen fertilizers (producing N2O), livestock digestion (producing methane from cows), and land-use changes like peatland clearing.",
  "how can cities reduce carbon emissions": "Cities can reduce emissions by promoting public transportation, developing green infrastructure, improving building energy efficiency, managing waste properly, and using renewable energy sources.",
  "what is carbon credit": "A carbon credit is a permit that allows the holder to emit one ton of carbon dioxide. These can be traded, allowing companies to buy 'rights' to emit or sell their 'emission savings'.",
  "how is meat consumption related to carbon emissions": "Meat production, especially red meat, requires large amounts of land, water, and feed. Livestock also produce methane. Reducing meat consumption can significantly decrease personal carbon footprint.",
  "how can smart technology help reduce emissions": "Smart technologies like smart grids, IoT sensors for building energy efficiency, transportation route optimization, and data analytics for energy prediction can help cut emissions.",
  "what is energy transition": "Energy transition is the global shift from fossil fuel-based energy systems to sustainable energy systems that rely on renewable sources and low-carbon technologies.",
  "what is the impact of carbon emissions on marine life": "Increased atmospheric CO2 causes oceans to absorb more CO2, leading to ocean acidification. This harms shellfish, coral reefs, and other marine ecosystems.",
  "what is blue carbon": "Blue carbon refers to carbon stored in coastal and marine ecosystems such as mangroves, seagrass meadows, and salt marshes. These ecosystems are highly effective at absorbing and storing carbon.",
  "how do reforestation and afforestation reduce emissions": "Reforestation (replanting forests) and afforestation (planting forests on non-forested land) help absorb CO2 from the atmosphere through photosynthesis, storing it in biomass and soil.",
  "what is climate change mitigation": "Climate change mitigation refers to actions taken to reduce or absorb greenhouse gas emissions, aiming to slow down or stop global warming.",
  "how is sustainable development related to carbon emissions": "Sustainable development aims to meet present needs without compromising future generations. It includes reducing carbon emissions through environmentally responsible economic and social practices.",
  "what is renewable energy (EBT)": "EBT stands for Renewable Energy, which comes from sustainable natural processes like solar, wind, hydro, geothermal, biomass, and wave energy. Its development is vital to reducing carbon emissions.",
  "what is the role of banks in supporting emissions reduction": "Banks can support emission reduction by providing loans for renewable energy projects, funding green initiatives, offering sustainable financial products, and adopting environmentally responsible investment policies."
}

kb_keys = list(KNOWLEDGE_BASE.keys())

vectorizer = TfidfVectorizer()
kb_vectors = vectorizer.fit_transform(kb_keys)

def get_response(input_message):
    if not input_message.strip():
        return "sorry, i dont understand"

    input_message = input_message.lower()
    input_vector = vectorizer.transform([input_message])
    similarities = cosine_similarity(input_vector, kb_vectors)[0]

    best_index = similarities.argmax()
    best_score = similarities[best_index]

    if best_score >= 0.3:  
        return KNOWLEDGE_BASE[kb_keys[best_index]]
    else:
        return "sorry, i dont understand"

def send_message():
    message = message_entry.get().strip()
    if message:
        chat_area.config(state="normal")
        chat_area.insert(tk.END, "You: " + message + "\n\n", "user")

        bot_response = get_response(message)
        chat_area.insert(tk.END, "Bot: " + bot_response + "\n\n", "bot")

        chat_area.config(state="disabled")
        chat_area.see(tk.END)
        message_entry.delete(0, tk.END)

def send_message_event(event):
    send_message()

root = tk.Tk()
root.title("Taman Rama Chatbot")
root.geometry("600x600")
root.resizable(False, False)
root.configure(bg="#211F24")

style = ttk.Style()
style.theme_use("clam")
style.configure(
    "Vertical.TScrollbar",
    background="#2F2C35",
    troughcolor="#211F24",
    bordercolor="#2F2C35",
    arrowcolor="white"
)

chat_frame = tk.Frame(root, bg="#211F24")
chat_frame.pack(padx=20, pady=20, fill="both", expand=True)

chat_area = tk.Text(
    chat_frame,
    height=20,
    width=60,
    state="disabled",
    bg="#2F2C35",
    fg="white",
    font=("Arial", 14),
    relief="flat",
    wrap="word"
)
chat_area.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(
    chat_frame,
    orient="vertical",
    command=chat_area.yview,
    style="Vertical.TScrollbar"
)
scrollbar.pack(side="right", fill="y")
chat_area.config(yscrollcommand=scrollbar.set)

chat_area.tag_config("user", foreground="#8DE0A7", font=("Arial", 14, "bold"))
chat_area.tag_config("bot", foreground="#BB86FC", font=("Arial", 14))

input_frame = tk.Frame(root, bg="#211F24")
input_frame.pack(padx=20, pady=(0, 20), fill="x")

message_entry = tk.Entry(
    input_frame,
    width=50,
    bg="#3C393F",
    fg="white",
    insertbackground="white",
    relief="flat",
    font=("Arial", 15),
    highlightbackground="#555555",
    highlightthickness=1
)
message_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
message_entry.bind("<Return>", send_message_event)

send_button = tk.Button(
    input_frame,
    text="Send",
    bg="#9B59B6",
    fg="black",
    relief="flat",
    font=("Arial", 15, "bold"),
    padx=15,
    pady=8,
    command=send_message
)
send_button.pack(side="right")

root.mainloop()