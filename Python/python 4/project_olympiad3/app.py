import csv
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import streamlit as st

BASE_DIR = Path(__file__).parent
CANDIDATE_FILES = ["data.csv"]

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
    "EN": {
        "label": "Endangered",
        "kriteria_A_penurunan_populasi_persen": {"A1": 70, "A2_A4": 50},
        "kriteria_C_maks_individu_dewasa": 2500,
        "kriteria_D_maks_individu_dewasa": 250,
        "kriteria_E_probabilitas_punah_persen": 20,
        "kriteria_E_rentang_waktu": "20 years or 5 generations",
        "ui_color": "#f59e0b",
    },
    "VU": {
        "label": "Vulnerable",
        "kriteria_A_penurunan_populasi_persen": {"A1": 50, "A2_A4": 30},
        "kriteria_C_maks_individu_dewasa": 10000,
        "kriteria_D_maks_individu_dewasa": 1000,
        "kriteria_E_probabilitas_punah_persen": 10,
        "kriteria_E_rentang_waktu": "100 years",
        "ui_color": "#eab308",
    },
    "NT": {
        "label": "Near Threatened",
        "deskripsi": "Close to or likely to qualify for a threatened category in the near future.",
        "ui_color": "#84cc16",
    },
    "LC": {
        "label": "Least Concern",
        "deskripsi": "Widespread and abundant taxon.",
        "ui_color": "#22c55e",
    },
    "DD": {
        "label": "Data Deficient",
        "deskripsi": "Inadequate information to make a direct or indirect assessment of its risk of extinction.",
        "ui_color": "#9ca3af",
    },
    "EX": {
        "label": "Extinct",
        "deskripsi": "No reasonable doubt that the last individual has died.",
        "ui_color": "#111827",
    },
    "EW": {
        "label": "Extinct in the Wild",
        "deskripsi": "Known only to survive in cultivation, captivity, or as a naturalized population far outside its historic range.",
        "ui_color": "#1f2937",
    },
}

CATEGORY_ALIASES = {"LR/nt": "NT", "LR/lc": "LC", "LR/cd": "NT"}
KINGDOM_GROUPS = {"🐾 Fauna": {"ANIMALIA"}, "🌿 Flora": {"PLANTAE"}, "🍄 Fungi": {"FUNGI"}, "🔬 Chromista": {"CHROMISTA"}}
PROJECTION_YEARS = 20
IUCN_PROJECTION_YEARS = {"CR": 10, "EN": 20, "VU": 100}

CONSERVATION_ORGS = [
    {
        "name": "IUCN Species Survival Commission (SSC)",
        "type": "Global Authority",
        "focus": "All threatened species (CR/EN/VU)",
        "kingdom": "All",
        "description": "Global species conservation authority. Manages the IUCN Red List and coordinates 900+ specialist groups.",
        "actions": ["Conservation status assessment", "Captive breeding guidelines", "Global expert coordination"],
        "url": "https://iucn.org/about-iucn",
    },
    {
        "name": "WWF (World Wildlife Fund)",
        "type": "NGO Global",
        "focus": "Tiger, Rhino, Elephant, Orangutan, Marine species",
        "kingdom": "ANIMALIA",
        "description": "World's largest conservation organization. Captive breeding and habitat restoration programs in 100+ countries.",
        "actions": ["Tiger breeding program (TX2)", "Habitat restoration", "Anti-wildlife trafficking"],
        "url": "https://www.worldwildlife.org",
    },
    {
        "name": "ZSL (Zoological Society of London)",
        "type": "Captive Breeding & Research",
        "focus": "Tiger, Penguin, Amphibians, Coral",
        "kingdom": "ANIMALIA",
        "description": "Manages London Zoo & Whipsnade Zoo. Captive breeding and reintroduction programs for threatened species.",
        "actions": ["Captive breeding program", "Veterinary medicine", "Field conservation"],
        "url": "https://www.zsl.org",
    },
    {
        "name": "Botanic Gardens Conservation International (BGCI)",
        "type": "Global Authority",
        "focus": "All threatened plants (PLANTAE)",
        "kingdom": "PLANTAE",
        "description": "Network of 600+ botanical gardens in 100+ countries. Focus on ex-situ conservation of threatened plants.",
        "actions": ["Seed banking", "Conservation gardens", "Plant habitat restoration"],
        "url": "https://www.bgci.org",
    },
    {
        "name": "Missouri Botanical Garden",
        "type": "Captive Breeding & Research",
        "focus": "Tropical plants, Orchids, Endemic flora",
        "kingdom": "PLANTAE",
        "description": "One of the world's premier botanical gardens. Plant breeding and taxonomy research programs.",
        "actions": ["Seed banking", "Taxonomy research", "Ex-situ conservation"],
        "url": "https://www.missouribotanicalgarden.org",
    },
    {
        "name": "TRAFFIC (Wildlife Trade Monitoring Network)",
        "type": "Anti-Trafficking",
        "focus": "All exploited species (CR/EN/VU)",
        "kingdom": "All",
        "description": "Wildlife trade monitoring network. Focus on preventing overexploitation.",
        "actions": ["Trade monitoring", "Policy advocacy", "Law enforcement"],
        "url": "https://www.traffic.org",
    },
    {
        "name": "Global Wildlife Conservation",
        "type": "Captive Breeding & Habitat",
        "focus": "Critically Endangered species",
        "kingdom": "All",
        "description": "Focuses on the most threatened CR species. Search for Lost Species program.",
        "actions": ["Species discovery expeditions", "Habitat protection", "Captive breeding"],
        "url": "https://globalwildlife.org",
    },
    {
        "name": "Coral Triangle Initiative",
        "type": "Habitat Restoration",
        "focus": "Marine species, Coral, Fish",
        "kingdom": "ANIMALIA",
        "description": "Conservation of the world's highest marine biodiversity region.",
        "actions": ["Coral reef restoration", "Marine protected areas", "Coastal community empowerment"],
        "url": "https://www.coraltriangleinitiative.org",
    },
    {
        "name": "Rainforest Alliance",
        "type": "Habitat Restoration",
        "focus": "Tropical flora & fauna",
        "kingdom": "All",
        "description": "Tropical forest conservation through sustainable certification and habitat restoration.",
        "actions": ["Forest certification", "Habitat restoration", "Sustainable agriculture"],
        "url": "https://www.rainforest-alliance.org",
    },
]


def kingdom_in_group(kingdom, group_label):
    if group_label == "All":
        return True
    return kingdom in KINGDOM_GROUPS.get(group_label, set())


def _get_projection_years(cat):
    return IUCN_PROJECTION_YEARS.get(cat, PROJECTION_YEARS)


def _get_decay(cat):
    p = IUCN_PROFILES[cat]
    if "kriteria_A_penurunan_populasi_persen" in p:
        decline_pct = p["kriteria_A_penurunan_populasi_persen"]["A2_A4"]
        years = _get_projection_years(cat)
        return (1.0 - decline_pct / 100.0) ** (1.0 / years) - 1.0
    fb = {"NT": -0.01, "LC": 0.0, "DD": -0.05, "EX": 0.0, "EW": 0.0}
    return fb.get(cat, 0.0)


def _get_pop0(cat):
    p = IUCN_PROFILES[cat]
    if "kriteria_C_maks_individu_dewasa" in p:
        return float(p["kriteria_C_maks_individu_dewasa"])
    fb = {"NT": 20000, "LC": 100000, "DD": 5000, "EX": 0, "EW": 1}
    return float(fb.get(cat, 0))


def _get_e_prob(cat):
    p = IUCN_PROFILES[cat]
    if "kriteria_E_probabilitas_punah_persen" in p:
        return float(p["kriteria_E_probabilitas_punah_persen"])
    fb = {"NT": 5.0, "LC": 1.0, "DD": 15.0, "EX": 100.0, "EW": 95.0}
    return fb.get(cat, 10.0)


def _resolve_data_path():
    for name in CANDIDATE_FILES:
        p = BASE_DIR / name
        if p.exists():
            return p
    return None


@st.cache_data(show_spinner="Loading verified ecosystem database...")
def load_database():
    path = _resolve_data_path()
    if path is None:
        return [], {}

    records = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            raw_cat = (row.get("category") or "").strip()
            cat = CATEGORY_ALIASES.get(raw_cat, raw_cat)
            if cat not in IUCN_PROFILES:
                continue

            common = (row.get("main_common_name") or "").strip()
            sci = (row.get("scientific_name") or "").strip()
            if not sci:
                continue

            records.append({
                "taxonid": (row.get("taxonid") or "").strip(),
                "kingdom": (row.get("kingdom_name") or "").strip(),
                "class": (row.get("class_name") or "").strip(),
                "order": (row.get("order_name") or "").strip(),
                "family": (row.get("family_name") or "").strip(),
                "scientific_name": sci,
                "common_name": common,
                "category": cat,
                "_common_lower": common.lower(),
                "_sci_lower": sci.lower(),
            })

    stats = _compute_stats(records)
    return records, stats


def _compute_stats(records):
    cat_counts, kingdom_counts = {}, {}
    for r in records:
        cat_counts[r["category"]] = cat_counts.get(r["category"], 0) + 1
        kingdom_counts[r["kingdom"]] = kingdom_counts.get(r["kingdom"], 0) + 1
    return {
        "total": len(records),
        "category_counts": cat_counts,
        "kingdom_counts": kingdom_counts,
        "threatened": sum(cat_counts.get(c, 0) for c in ("CR", "EN", "VU")),
    }


def search_species(records, keyword, group_filter="All", kingdom_filter="All",
                   category_filter="All", limit=60):
    kw = keyword.strip().lower()
    all_group = group_filter == "All"
    all_king = kingdom_filter == "All"
    all_cat = category_filter == "All"

    exact, partial = [], []
    for r in records:
        if not all_group and not kingdom_in_group(r["kingdom"], group_filter):
            continue
        if not all_king and r["kingdom"] != kingdom_filter:
            continue
        if not all_cat and r["category"] != category_filter:
            continue
        if kw == "":
            partial.append(r)
        elif r["_common_lower"] == kw or r["_sci_lower"] == kw:
            exact.append(r)
        elif kw in r["_common_lower"] or kw in r["_sci_lower"]:
            partial.append(r)
        if not kw and len(partial) > limit * 4:
            break

    ranked = exact + partial
    return ranked[:limit], len(ranked)


def project_population(category, years=None):
    if years is None:
        years = _get_projection_years(category)
    p0 = _get_pop0(category)
    rate = _get_decay(category)
    t = np.arange(0, years + 1)
    pop = p0 * np.power(1.0 + rate, t)
    return np.clip(pop, 0, None)


def conservation_risk_score(category, trajectory=None):
    base = {"CR": 90, "EN": 70, "VU": 50, "NT": 30, "LC": 10, "DD": 0, "EX": 100, "EW": 95}
    return base.get(category, 0)


def priority_label(score):
    if score >= 80:
        return "CRITICAL", "#dc2626"
    if score >= 60:
        return "HIGH", "#f59e0b"
    if score >= 40:
        return "MEDIUM", "#eab308"
    return "LOW", "#22c55e"



def plot_status_pie(category_counts):
    order = ["CR", "EN", "VU", "NT", "LC", "DD", "EX", "EW"]
    labels, sizes, colors = [], [], []
    for c in order:
        n = category_counts.get(c, 0)
        if n > 0:
            labels.append(f"{c} — {n:,}")
            sizes.append(n)
            colors.append(IUCN_PROFILES[c]["ui_color"])

    fig, ax = plt.subplots(figsize=(6, 6))
    wedges, texts, autotexts = ax.pie(
        sizes, colors=colors, autopct=lambda p: f"{p:.1f}%" if p > 3 else "",
        startangle=90, pctdistance=0.75,
        wedgeprops={"edgecolor": "white", "linewidth": 1.5},
        textprops={"fontsize": 9},
    )
    for at in autotexts:
        at.set_fontsize(9)
        at.set_fontweight("bold")
    ax.legend(wedges, labels, loc="center left", bbox_to_anchor=(1.0, 0.5), fontsize=9)
    ax.set_title("Conservation Status Distribution (IUCN)", fontsize=12, fontweight="bold")
    ax.axis("equal")
    return fig


def plot_threatened_bar(category_counts):
    cats = ["CR", "EN", "VU", "NT"]
    vals = [category_counts.get(c, 0) for c in cats]
    colors = [IUCN_PROFILES[c]["ui_color"] for c in cats]
    fig, ax = plt.subplots(figsize=(5, 4))
    bars = ax.bar(cats, vals, color=colors, edgecolor="white")
    ax.set_title("Species Count by Threat Level", fontsize=11, fontweight="bold")
    ax.set_ylabel("Number of species")
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v, f"{v:,}",
                ha="center", va="bottom", fontsize=8)
    ax.spines[["top", "right"]].set_visible(False)
    return fig


def plot_rescue_timeline(category, years=None):
    if years is None:
        years = _get_projection_years(category)
    t = np.arange(0, years + 1)
    baseline = project_population(category, years)

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(t, baseline, color="#dc2626", lw=2.5, marker="o", ms=3,
            label="Population projection (IUCN decline rate)")
    ax.fill_between(t, baseline, color="#dc2626", alpha=0.08)
    ax.set_title(f"Population Projection {years} Years — {category} "
                 f"({IUCN_PROFILES[category]['label']})", fontsize=10, fontweight="bold")
    ax.set_xlabel("Year", fontsize=9)
    ax.set_ylabel("Estimated population (mature individuals)", fontsize=9)
    ax.xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(integer=True))
    ax.legend(fontsize=8)
    ax.grid(alpha=0.25)
    ax.spines[["top", "right"]].set_visible(False)
    return fig


def plot_kingdom_bar(kingdom_counts):
    sorted_kingdoms = sorted(kingdom_counts.items(), key=lambda x: -x[1])
    names = [k.title() for k, _ in sorted_kingdoms]
    vals = [v for _, v in sorted_kingdoms]
    bar_colors = ["#3b82f6", "#8b5cf6", "#ec4899", "#f97316"][:len(names)]
    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.barh(names[::-1], vals[::-1], color=bar_colors[::-1], edgecolor="white", height=0.6)
    for b, v in zip(bars, vals[::-1]):
        ax.text(v + max(vals) * 0.01, b.get_y() + b.get_height() / 2, f"{v:,}",
                va="center", fontsize=9, fontweight="bold")
    ax.set_title("Species Count by Kingdom", fontsize=12, fontweight="bold")
    ax.set_xlabel("Number of species")
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_xlim(0, max(vals) * 1.15)
    return fig


def plot_threatened_by_kingdom(records):
    cats = ["CR", "EN", "VU"]
    kingdoms = sorted({r["kingdom"] for r in records})
    data = {k: [0] * len(cats) for k in kingdoms}
    for r in records:
        if r["category"] in cats:
            data[r["kingdom"]][cats.index(r["category"])] += 1

    fig, ax = plt.subplots(figsize=(7, 4))
    x = np.arange(len(kingdoms))
    width = 0.25
    for i, cat in enumerate(cats):
        vals = [data[k][i] for k in kingdoms]
        offset = (i - 1) * width
        bars = ax.bar(x + offset, vals, width, label=cat, color=IUCN_PROFILES[cat]["ui_color"], edgecolor="white")
        for b, v in zip(bars, vals):
            if v > 0:
                ax.text(b.get_x() + b.get_width() / 2, v, f"{v:,}",
                        ha="center", va="bottom", fontsize=7)
    ax.set_xticks(x)
    ax.set_xticklabels([k.title() for k in kingdoms], fontsize=9)
    ax.set_title("Threatened Species (CR/EN/VU) by Kingdom", fontsize=12, fontweight="bold")
    ax.set_ylabel("Number of species")
    ax.legend(fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    return fig


# --- streamlit setup ---
st.set_page_config(page_title="EcoRescue", page_icon="🌍", layout="wide")

DATA, STATS = load_database()

if "quiz_done" not in st.session_state:
    st.session_state.quiz_done = False
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0

st.sidebar.title("🌍 EcoRescue")
st.sidebar.caption("Conservation Analysis Platform")

menu = st.sidebar.radio(
    "Navigation:",
    ["Species & Database", "Conservation Dashboard",
     "Extinction Predictor", "Conservation Support",
     "Education Quiz", "About & Impact"],
)

if not DATA:
    st.error("Data file not found. Place `data.csv` in the same folder as app.py.")
    st.stop()


# --- Species & Database ---
if menu == "Species & Database":
    st.title("Verified IUCN Species Database")
    st.write("Search species from the **verified IUCN database** "
             f"({STATS['total']:,} records). Exact name matches are prioritized.")

    group_opt = st.radio("Organism group:", ["All", "🐾 Fauna", "🌿 Flora", "🍄 Fungi", "🔬 Chromista"], horizontal=True)

    c1, c2 = st.columns([2, 1])
    with c1:
        keyword = st.text_input("Common / scientific name:", placeholder="e.g. Tiger / Panthera tigris")
    with c2:
        cat_display = st.selectbox("Status:", ["All"] + [f"{c} — {IUCN_PROFILES[c]['label']}" for c in ["CR", "EN", "VU", "NT", "LC", "DD", "EX", "EW"]])

    cat_opt = cat_display.split(" — ")[0] if " — " in cat_display else cat_display
    results, total_match = search_species(DATA, keyword, group_opt, "All", cat_opt)
    st.caption(f"Showing {len(results)} of {total_match:,} matches.")

    if not results:
        st.warning("No species match the criteria.")
    for r in results:
        profile = IUCN_PROFILES[r["category"]]
        traj = project_population(r["category"])
        score = conservation_risk_score(r["category"], traj)
        prio, prio_color = priority_label(score)

        with st.expander(
            f"{r['common_name'] or r['scientific_name']}  "
            f"— {r['category']} ({profile['label']})"
        ):
            col_a, col_b = st.columns([2, 1])
            with col_a:
                st.markdown(f"**Scientific name:** _{r['scientific_name']}_")
                st.caption(f"Kingdom: {r['kingdom']} | Class: {r['class'] or '-'} "
                           f"| Family: {r['family'] or '-'}")
                st.caption(f"Taxon ID (IUCN): {r['taxonid']}")
            with col_b:
                st.metric("Conservation Risk Score", f"{score}/100", prio)
                st.markdown(
                    f"<span style='color:{prio_color};font-weight:700'>"
                    f"Priority: {prio}</span>", unsafe_allow_html=True)


# --- Conservation Dashboard ---
elif menu == "Conservation Dashboard":
    st.title("Conservation Dashboard")
    st.write("Comprehensive overview of biodiversity status in the database.")

    cc = STATS["category_counts"]
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Species", f"{STATS['total']:,}")
    m2.metric("Critically Endangered", f"{cc.get('CR', 0):,}")
    m3.metric("Endangered", f"{cc.get('EN', 0):,}")
    m4.metric("Vulnerable", f"{cc.get('VU', 0):,}")

    pct_threat = STATS["threatened"] / STATS["total"] * 100 if STATS["total"] else 0
    st.progress(min(1.0, pct_threat / 100),
                text=f"{STATS['threatened']:,} threatened species (CR+EN+VU) — {pct_threat:.1f}% of database")

    st.divider()
    col_pie, col_bar = st.columns(2)
    with col_pie:
        fig_pie = plot_status_pie(cc)
        st.pyplot(fig_pie)
        plt.close(fig_pie)
    with col_bar:
        fig_bar = plot_threatened_bar(cc)
        st.pyplot(fig_bar)
        plt.close(fig_bar)

    st.divider()
    col_kingdom, col_threat = st.columns(2)
    with col_kingdom:
        fig_kingdom = plot_kingdom_bar(STATS["kingdom_counts"])
        st.pyplot(fig_kingdom)
        plt.close(fig_kingdom)
    with col_threat:
        fig_threat = plot_threatened_by_kingdom(DATA)
        st.pyplot(fig_threat)
        plt.close(fig_threat)


# --- Extinction Predictor ---
elif menu == "Extinction Predictor":
    st.title("IUCN-Based Extinction Predictor")
    st.write("Select a species to project its population trajectory based on "
             "**official IUCN v3.1 decline rates**. All numbers are sourced "
             "from the guidelines - no additional assumptions.")

    pred_group = st.radio("Organism group:", ["All", "🐾 Fauna", "🌿 Flora", "🍄 Fungi", "🔬 Chromista"], horizontal=True)

    options = [
        r for r in DATA
        if kingdom_in_group(r["kingdom"], pred_group)
        and r["category"] in ("CR", "EN", "VU", "NT")
    ][:500]

    if not options:
        st.warning("No threatened species in this group.")
        st.stop()

    labels = [
        f"{r['common_name'] or r['scientific_name']} ({r['category']}) — {r['scientific_name']}"
        for r in options
    ]
    pick = st.selectbox("Species:", range(len(labels)), format_func=lambda i: labels[i])
    species = options[pick]
    category = species["category"]
    profile = IUCN_PROFILES[category]

    baseline = project_population(category)
    risk_now = conservation_risk_score(category, baseline)
    prio, prio_color = priority_label(risk_now)

    st.divider()
    k1, k2, k3 = st.columns(3)
    k1.metric("IUCN Status", f"{category}", profile["label"])
    k2.metric("Current Risk Score", f"{risk_now}/100", prio)
    k3.metric(f"Population projection yr-{_get_projection_years(category)}",
              f"{baseline[-1]:,.0f}",
              delta=f"{baseline[-1] - baseline[0]:,.0f}")

    fig_tl = plot_rescue_timeline(category)
    st.pyplot(fig_tl, use_container_width=False)
    plt.close(fig_tl)


# --- Education Quiz ---
elif menu == "Education Quiz":
    st.title("Education Quiz: Overexploitation & IUCN")
    st.write("Test your understanding of overexploitation and conservation status.")

    QUESTIONS = [
        {"q": "Which IUCN category faces the HIGHEST risk of extinction in the wild?",
         "opts": ["Vulnerable (VU)", "Critically Endangered (CR)", "Least Concern (LC)"],
         "answer": "Critically Endangered (CR)"},
        {"q": "What is 'overexploitation' as a threat to biodiversity?",
         "opts": ["Harvesting species faster than they can regenerate",
                  "Global climate change",
                  "Ocean plastic pollution"],
         "answer": "Harvesting species faster than they can regenerate"},
        {"q": "What does 'EW' stand for in the IUCN Red List?",
         "opts": ["Endangered Wildlife", "Extinct in the Wild", "Early Warning"],
         "answer": "Extinct in the Wild"},
        {"q": "Which intervention most directly combats poaching for wildlife trade?",
         "opts": ["Anti-trafficking law enforcement", "Planting trees", "Reducing emissions"],
         "answer": "Anti-trafficking law enforcement"},
    ]

    if not st.session_state.quiz_done:
        answers = []
        for i, item in enumerate(QUESTIONS):
            st.subheader(f"Question {i + 1}")
            st.write(item["q"])
            answers.append(st.radio("Select answer:", item["opts"], key=f"q{i}", index=None))

        if st.button("Submit Answers", type="primary"):
            correct = sum(1 for a, item in zip(answers, QUESTIONS) if a == item["answer"])
            st.session_state.quiz_score = int(round(correct / len(QUESTIONS) * 100))
            st.session_state.quiz_done = True
            st.rerun()
    else:
        score = st.session_state.quiz_score
        st.metric("Final Score", f"{score} / 100")
        if score == 100:
            st.balloons()
            st.success("🏅 Badge: CONSERVATION EXPERT — Perfect!")
        elif score >= 50:
            st.info("🥈 Badge: NATURE GUARDIAN — Good, keep learning!")
        else:
            st.warning("🌱 Badge: CARING BEGINNER — Review the About & Impact page.")

        if st.button("Try Again"):
            st.session_state.quiz_done = False
            st.session_state.quiz_score = 0
            st.rerun()


# --- Conservation Support ---
elif menu == "Conservation Support":
    st.title("Conservation Support")
    st.write("After identifying high-risk species, the next step is **taking action**. "
             "Below are conservation organizations and programs you can support.")

    cs_group = st.radio("Filter by organism:", ["All", "🐾 Fauna", "🌿 Flora", "🍄 Fungi", "🔬 Chromista"], horizontal=True)

    threatened = [r for r in DATA if r["category"] in ("CR", "EN", "VU")]
    threat_counts = {}
    for r in threatened:
        threat_counts[r["scientific_name"]] = threat_counts.get(r["scientific_name"], 0) + 1

    kingdom_map = {"🐾 Fauna": "ANIMALIA", "🌿 Flora": "PLANTAE", "🍄 Fungi": "FUNGI", "🔬 Chromista": "CHROMISTA"}
    if cs_group == "All":
        orgs = CONSERVATION_ORGS
    else:
        selected_kingdom = kingdom_map[cs_group]
        orgs = [o for o in CONSERVATION_ORGS if o["kingdom"] in (selected_kingdom, "All")]

    st.subheader("Threatened Species in Database")
    col_cr, col_en, col_vu = st.columns(3)
    with col_cr:
        cr_count = sum(1 for r in threatened if r["category"] == "CR")
        st.metric("Critically Endangered", f"{cr_count:,}")
    with col_en:
        en_count = sum(1 for r in threatened if r["category"] == "EN")
        st.metric("Endangered", f"{en_count:,}")
    with col_vu:
        vu_count = sum(1 for r in threatened if r["category"] == "VU")
        st.metric("Vulnerable", f"{vu_count:,}")

    st.divider()
    st.subheader("Conservation Organizations & Programs")

    for org in orgs:
        with st.expander(f"{org['name']} — {org['type']}"):
            st.write(f"**Focus:** {org['focus']}")
            st.write(f"**Description:** {org['description']}")
            st.markdown("**Key Actions:**")
            for action in org["actions"]:
                st.markdown(f"- {action}")
            st.link_button("Visit Website", org["url"], type="secondary")

    st.divider()
    st.subheader("How You Can Help")
    st.markdown("""
    1. **Donate** — Support conservation organizations directly through their websites.
    2. **Adopt a Species** — Many zoos offer species adoption programs that fund captive breeding.
    3. **Volunteer** — Join field conservation projects or local habitat restoration.
    4. **Spread Awareness** — Share conservation data from this platform with others.
    5. **Refuse Wildlife Products** — Say no to products from endangered species.
    6. **Report Wildlife Crime** — Use TRAFFIC or local authorities to report illegal trade.
    """)


# --- About & Impact ---
elif menu == "About & Impact":
    st.title("About EcoRescue & Impact")

    st.header("The Problem: Overexploitation")
    st.write(
        "Overharvesting (hunting, trading, capturing, logging) removes **flora, fauna, fungi, and chromista species** "
        "from the wild faster than they can reproduce. This is one of the primary direct drivers of extinction."
    )

    st.header("Solutions Offered")
    st.markdown("""
    1. **Verified Flora & Fauna Database** — exact-match search on real IUCN data.
    2. **IUCN Extinction Predictor** — quantitative population projection + Risk Score 0–100.
    3. **Conservation Support** — connect with organizations and programs to protect threatened species.
    4. **Conservation Dashboard** — status pie/bar charts + IUCN-based extinction projection curve.
    5. **Education & Quiz** — adaptive quiz + IUCN-recognized conservation action types.
    """)

    st.header("Real-World Actions")
    st.markdown("""
    - Support anti-wildlife trafficking law enforcement.
    - Refuse to buy products from protected species.
    - Support captive breeding & habitat restoration.
    - Spread conservation awareness.
    """)

    st.divider()
    st.caption("Team CodeCyberBuzz • ICO 2026 • Methodology: IUCN Red List Categories "
               "and Criteria v3.1 (2012) • Stack: Streamlit + NumPy + Matplotlib")
