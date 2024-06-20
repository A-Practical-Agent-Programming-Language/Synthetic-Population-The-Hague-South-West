household_data_code_map = {
    'Geslacht': 'gender',
    'Leeftijd': 'age_group',
    'Regio\'s': 'region',
    'Perioden': 'period',
    'Totaal personen in huishoudens (aantal)': 'total_members',
    'Personen in particuliere huishoudens/Totaal in particuliere huishoudens (aantal)': 'total_private_members',
    'Personen in particuliere huishoudens/Thuiswonend kind (aantal)': 'child',
    'Personen in particuliere huishoudens/Alleenstaand (aantal)': 'single',
    'Personen in particuliere huishoudens/Samenwonend/Totaal samenwonende personen (aantal)': 'living_together',
    'Personen in particuliere huishoudens/Samenwonend/Partner in niet-gehuwd paar zonder ki... (aantal)':
        'non_married_no_children',
    'Personen in particuliere huishoudens/Samenwonend/Partner in gehuwd paar zonder kinderen (aantal)':
        'married_no_children',
    'Personen in particuliere huishoudens/Samenwonend/Partner in niet-gehuwd paar met kinderen (aantal)':
        'non_married_with_children',
    'Personen in particuliere huishoudens/Samenwonend/Partner in gehuwd paar met kinderen (aantal)':
        'married_with_children',
    'Personen in particuliere huishoudens/Ouder in eenouderhuishouden (aantal)': 'single_parent',
    'Personen in particuliere huishoudens/Overig lid huishouden (aantal)': 'additional_members',
    'Personen in institutionele huishoudens (aantal)': 'institutional_members',
}

specific_to_grouped_education_map = {
    "Basisonderwijs": "primary",
    "Speciaal basisonderwijs": "primary",
    "Speciale scholen": "primary",
    "Vo algemene leerjaren 1-3": "low",
    "Vwo 3-6": "middle",
    "Havo 3-5": "middle",
    "Vmbo theoretische-gemengde leerweg 3-4": "low",
    "Vmbo basis-kaderberoeps 3-4": "low",
    "Praktijkonderwijs": "low",
    "Vavo": "middle",
    "Mbo bol": "middle",
    "Mbo bbl": "middle",
    "Assistentopleiding (niveau 1)": "low",
    "Basisberoepsopleiding (niveau 2)": "middle",
    "Vakopleiding (niveau 3)": "middle",
    "Middenkaderopleiding (niveau 4a)": "middle",
    "Specialistenopleiding (niveau 4b)": "middle",
    "Hoger beroepsonderwijs": "high",
    "Wetenschappelijk onderwijs": "high",
}

specific_to_grouped_attained_education_map = {
    'no_education': 'low',
    '111 Basisonderwijs': 'low',
    '121 Vmbo-b/k, mbo1': 'low',
    '122 Vmbo-g/t, havo-, vwo-onderbouw': 'low',

    '211 Mbo2 en mbo3': 'middle',
    '212 Mbo4': 'middle',
    '213 Havo, vwo': 'middle',

    '311 Hbo-, wo-bachelor': 'high',
    '321 Hbo-, wo-master, doctor': 'high',
}

household_map = {
    'child_in_married_with_1_children': 'in_hh_with_children',
    'child_in_married_with_2_children': 'in_hh_with_children',
    'child_in_married_with_3_children': 'in_hh_with_children',
    'married_no_children': 'in_hh_without_children',
    'married_with_1_children': 'in_hh_with_children',
    'married_with_2_children': 'in_hh_with_children',
    'married_with_3_children': 'in_hh_with_children',
    'non_married_no_children': 'in_hh_without_children',
    'non_married_with_2_children': 'in_hh_with_children',
    'single': 'single_person',
    'child_in_non_married_with_1_children': 'in_hh_with_children',
    'child_in_non_married_with_2_children': 'in_hh_with_children',
    'child_in_non_married_with_3_children': 'in_hh_with_children',
    'child_of_single_parent_1_children': 'in_hh_with_children',
    'child_of_single_parent_2_children': 'in_hh_with_children',
    'child_of_single_parent_3_children': 'in_hh_with_children',
    'non_married_with_1_children': 'in_hh_with_children',
    'non_married_with_3_children': 'in_hh_with_children',
    'single_parent_1_children': 'in_hh_with_children',
    'single_parent_2_children': 'in_hh_with_children',
    'single_parent_3_children': 'in_hh_with_children'
}
