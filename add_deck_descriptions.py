"""
add_deck_descriptions.py — One-time helper
Adds curated clinical descriptions to all 83 presentation entries in presentations.json.
Safe to re-run: only updates entries that are missing a description.
Run from the repository root.
"""

import json, os

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(REPO_ROOT, "landing-page", "data", "presentations.json")

# Keyed by exact href value from presentations.json
DESCRIPTIONS = {
    "decks/hydrops-fetalis-slides/hydrops_fetalis_slides.html":
        "Comprehensive guide to hydrops fetalis: immune vs. non-immune causes, ultrasound diagnosis, MCA Doppler for fetal anemia, management options, and perinatal prognosis.",
    "decks/cholestasis-of-pregnancy-icp/cholestasis-pregnancy-patient-education.html":
        "Covers intrahepatic cholestasis of pregnancy (ICP): bile acid elevation, intense pruritus, UDCA treatment, serial NST monitoring, and delivery timing by severity.",
    "decks/cystic-fibrosis-carrier/CF_Carrier_Consultation.html":
        "Explains CF carrier status: CFTR mutation inheritance, partner testing, reproductive risk (1-in-4 affected child if both carriers), and reproductive options.",
    "decks/multiple-anomalies-aneuploidy/fetal_anomalies_patient_education.html":
        "Addresses the significance of multiple fetal anomalies on ultrasound, aneuploidy risk stratification, amniocentesis counseling, and prognosis discussions.",
    "decks/missed-abortion/missed-abortion-patient-education.html":
        "Compassionate guide to missed abortion: ultrasound diagnosis, expectant vs. medical vs. surgical management, emotional support, and guidance for future pregnancies.",
    "decks/antidepressants-pregnancy/antidepressants_pregnancy_slideshow.html":
        "Covers SSRI and SNRI use in pregnancy: risks of untreated depression vs. medication exposure, neonatal adaptation syndrome, and shared decision-making guidance.",
    "decks/atrial-septal-aneurysm/atrial-septal-aneurysm.html":
        "Explains atrial septal aneurysm found on fetal echo: what it means, its association with other cardiac defects, postnatal follow-up, and expected outcomes.",
    "decks/isolated-third-ventricle-dilation/isolated-third-ventricle.html":
        "Explains isolated third ventricle dilation on fetal MRI/ultrasound: measurement criteria, differential diagnosis, monitoring protocols, and expected postnatal outcomes.",
    "decks/asthma-in-pregnancy/asthma-in-pregnancy.html":
        "Covers asthma management in pregnancy: medication safety (inhaled corticosteroids, albuterol), step-up therapy, peak flow monitoring, and avoiding asthma triggers.",
    "decks/tylenol-in-pregnancy/acetaminophen_pregnancy_patient_education.html":
        "Addresses acetaminophen safety in pregnancy: recommended dosing, duration limits, emerging neurodevelopmental research, and safer alternatives for pain management.",
    "decks/crohns-disease/crohns-disease.html":
        "Addresses IBD and Crohn's disease in pregnancy: medication safety (biologics, steroids), disease activity monitoring, nutritional support, and neonatal outcomes.",
    "decks/nuchal-nt-NIPT/nuchal-nt-NIPT.html":
        "Covers combined first trimester screening: nuchal translucency measurement, PAPP-A, free beta-hCG, and cfDNA NIPT — with interpretation guidance and follow-up options.",
    "decks/canibis-in-pregnancy/canibis-in-pregnancy.html":
        "Evidence-based guide to cannabis in pregnancy: fetal neurodevelopmental risks, low birth weight, NICU admission, and cessation counseling for patients using marijuana.",
    "decks/pregnancy-ramadan/pregnancy_ramadan_slides.html":
        "Culturally sensitive guide to Ramadan fasting in pregnancy: clinical risks of dehydration and hypoglycemia, Islamic exemptions, Suhoor/Iftar nutrition, and monitoring guidance.",
    "decks/chronic-hypertension-providers/chronic_hypertension_pregnancy.html":
        "Covers diagnosis, antihypertensive therapy selection, blood pressure targets, superimposed preeclampsia risk, and delivery timing for chronic hypertension in pregnancy.",
    "decks/hepatitis-c/hepatitis-c-pregnancy.html":
        "Covers hepatitis C in pregnancy: vertical transmission risk, breastfeeding guidance, neonatal testing protocols, and the role of direct-acting antiviral therapy postpartum.",
    "decks/hepatitis-b-in-pregnancy/hepatitis-b-in-pregnancy.html":
        "Explains hepatitis B in pregnancy: HBsAg screening, vertical transmission risk, antiviral therapy for high viral loads, and neonatal immunoprophylaxis at delivery.",
    "decks/late-prenatal-care/late-prenatal-care.html":
        "Addresses the clinical implications of initiating prenatal care after the first trimester: missed screenings, catch-up protocols, and risk assessment for late presenters.",
    "decks/pericardial-effusion/pericardial-effusion.html":
        "Covers fetal pericardial effusion: causes ranging from benign to hydrops, ultrasound measurement, associated anomalies, and management based on severity.",
    "decks/intracranial-hypertension-iih-pregnancy/iih_pregnancy_slides.html":
        "Explains idiopathic intracranial hypertension (pseudotumor cerebri) in pregnancy: headache, papilledema, lumbar puncture, acetazolamide safety, and delivery planning.",
    "decks/grand-multiparity/grand_multiparity.html":
        "Covers grand multiparity (\u22655 deliveries): uterine atony risk, placenta previa, malpresentation, and the importance of delivery planning at a facility with blood bank access.",
    "decks/lga-fetus/lga_counseling.html":
        "Addresses macrosomia diagnosis, shoulder dystocia risk counseling, delivery planning, and the role of gestational diabetes in LGA fetal growth.",
    "decks/fetal_arrhythmias/fetal_arrhythmias.html":
        "Explains fetal heart rhythm abnormalities including PACs, SVT, and heart block: causes, monitoring, treatment options, and when intervention is needed.",
    "decks/pyelectasis-patient-present/pyelectasis_patient_presentation.html":
        "Explains fetal pyelectasis (renal pelvis dilation): measurement thresholds, association with Down syndrome, postnatal follow-up, and when further workup is needed.",
    "decks/bilateral-renal-agenesis/bilateral_renal_agenesis_patient_education.html":
        "Explains bilateral renal agenesis (Potter sequence): absent kidneys, oligohydramnios, pulmonary hypoplasia, and compassionate counseling for this lethal fetal anomaly.",
    "decks/fetal-club-foot-deformity/clubfoot_patient_consultation-new.html":
        "Covers fetal clubfoot (talipes equinovarus): isolated vs. associated findings, postnatal Ponseti casting treatment, and counseling on long-term outcomes.",
    "decks/low-papp-a-test/low_papp_a_patient_presentation.html":
        "Explains low PAPP-A in the first trimester: its association with FGR, preeclampsia, and preterm birth \u2014 and the surveillance protocols recommended for affected pregnancies.",
    "decks/subchorionic-hematoma/subchorionic_hematoma_patient_education.html":
        "Covers subchorionic hematoma in early pregnancy: ultrasound findings, association with bleeding and pregnancy loss, activity restrictions, and prognosis by size.",
    "decks/morbid-obesity/morbid-obesity.html":
        "Explores maternal and fetal risks of morbid obesity in pregnancy, including gestational diabetes, preeclampsia, sleep apnea, and cesarean delivery considerations.",
    "decks/hemoglobinopathies/hemoglobin_traits_pregnancy_patient_education.html":
        "Comprehensive overview of hemoglobin variants in pregnancy, including sickle cell, thalassemia traits, and Hb C \u2014 with screening, diagnosis, and management guidance.",
    "decks/basic-gdm/gestational_diabetes_patient_guide.html":
        "Understand gestational diabetes: how it is diagnosed, how diet and medication control blood sugar, and what monitoring is needed to protect mother and baby.",
    "decks/placental-chorioangioma/placental_chorioangioma_presentation.html":
        "Covers placental chorioangioma: a benign vascular tumor of the placenta, its association with polyhydramnios and fetal anemia, and monitoring protocols.",
    "decks/fetal-growth-restriction-patients/index.html":
        "Explains fetal growth restriction (FGR): causes, ultrasound diagnosis, Doppler surveillance, and delivery timing to minimize risks of stillbirth and neonatal complications.",
    "decks/fibroids/index.html":
        "Covers uterine fibroids in pregnancy: impact on implantation, placentation, preterm labor, and cesarean risk \u2014 with monitoring recommendations and pain management.",
    "decks/type-1-diabetes/index.html":
        "Managing Type 1 diabetes in pregnancy: insulin adjustment, glucose targets, hypoglycemia prevention, fetal surveillance, and delivery planning for optimal outcomes.",
    "decks/type-2-diabetes/type2_diabetes_pregnancy.html":
        "Covers pregestational Type 2 diabetes management in pregnancy, including medication safety, glucose monitoring, fetal growth surveillance, and delivery timing.",
    "decks/nipt-testing/nipt-testing.html":
        "Explains cell-free DNA (cfDNA) NIPT: what chromosomal conditions it screens for, sensitivity and specificity, positive predictive value, and next steps after abnormal results.",
    "decks/hypocoiled-umbilical/hypocoiled-umbilical.html":
        "Explains hypo-coiled umbilical cord: coiling index measurement, association with adverse perinatal outcomes, and the surveillance approach for affected pregnancies.",
    "decks/complex-heart-defects/dilated_coronary_sinus_presentation.html":
        "Explains dilated coronary sinus and its association with persistent left superior vena cava (PLSVC), cardiac defects, and the recommended postnatal evaluation pathway.",
    "decks/external-cephalic-version-breech/breech_presentation_patient_guide.html":
        "Covers breech presentation at term: ECV success rates, contraindications, procedure steps, risks, and counseling on planned cesarean vs. vaginal breech delivery options.",
    "decks/chtn-and-morbid-obesity/chtn-and-morbid-obesity.html":
        "Addresses the compounded risks of chronic hypertension and morbid obesity in pregnancy, including cardiovascular monitoring, antihypertensive therapy, and delivery planning.",
    "decks/spinal-muscular-atrophy-carrier/sma_carrier_presentation.html":
        "Covers SMA carrier screening: SMN1 copy number analysis, recurrence risk, partner testing, and reproductive options including PGT-M and prenatal diagnosis.",
    "decks/fetal-echocardiography/fetal-echocardiography.html":
        "Comprehensive guide to fetal echocardiography: indications, four-chamber view, outflow tracts, Doppler assessment, and detection of congenital heart disease.",
    "decks/gestational-dating/gestational_dating_bootcamp.html":
        "Sonographer training on gestational age dating: CRL in the first trimester, BPD/HC/AC/FL in the second trimester, ACOG criteria for changing dates, and documentation standards.",
    "decks/short-interval-pregnancy/short-interval.html":
        "Explains interpregnancy interval: risks of spacing pregnancies less than 18 months apart, including preterm birth, FGR, and uterine rupture in prior cesarean patients.",
    "decks/dichorionic-twins/di-di-twins.html":
        "Explains Di-Di twin pregnancy: chorionicity determination, growth scan schedule, preterm birth risk, and delivery timing recommendations for dichorionic-diamniotic twins.",
    "decks/advanced-maternal-age-patient/advanced_maternal_age_patient_education.html":
        "Covers AMA (\u226535 years): age-related aneuploidy risk, NIPT and amniocentesis options, preeclampsia and GDM screening, and delivery planning for older mothers.",
    "decks/hlhs-sonography/hlhs_sonography.html":
        "Sonographer-focused guide to HLHS: ultrasound identification of left heart hypoplasia, associated findings, referral criteria, and fetal echocardiography indications.",
    "decks/gastric-bypass/gastric-bypass.html":
        "Covers nutritional deficiencies, dumping syndrome, fetal growth monitoring, and gestational weight gain guidance for pregnancies following bariatric surgery.",
    "decks/eif-patient/eif_patient_education_with_images.html":
        "Explains echogenic intracardiac focus (EIF): its minor marker status for aneuploidy, low positive predictive value in isolation, and guidance for patient counseling.",
    "decks/pyelectasis-hydronephrosis/pyelectasis_hydronephrosis_sonographer_presentation.html":
        "Sonographer training guide on measuring renal pelvis dilation, grading hydronephrosis, identifying associated anomalies, and optimizing fetal renal ultrasound technique.",
    "decks/hiv-pregnancy/hiv_pregnancy_presentation.html":
        "Comprehensive clinical guide to HIV in pregnancy: ART regimen selection, viral load targets, mode of delivery decisions, and neonatal prophylaxis to prevent vertical transmission.",
    "decks/anemia-in-pregnancy/anemia_in_pregnancy.html":
        "Covers iron-deficiency, folate, and B12 anemia in pregnancy: CBC interpretation, oral vs. IV iron therapy, dietary guidance, and when transfusion is indicated.",
    "decks/placenta-accreta-spectrum/pas-patient-education.html":
        "Explains placenta accreta, increta, and percreta: ultrasound diagnosis, risk factors (prior cesarean), planned delivery at a center of excellence, and hysterectomy counseling.",
    "decks/previous-myomectomy/pregnancy-following-myomectomy-slides.html":
        "Addresses pregnancy after myomectomy: uterine rupture risk stratification, mode of delivery counseling, and surveillance protocols based on depth of prior myometrial entry.",
    "decks/galactosemia-carrier-status/galactosemia_carrier_presentation.html":
        "Explains galactosemia carrier status: GALT gene mutations, autosomal recessive inheritance, partner testing, and implications for newborn screening and dietary management.",
    "decks/thyroid-manaagement-pregnancy/index2.html":
        "Covers hypothyroidism, hyperthyroidism, and thyroid antibody screening in pregnancy, including TSH targets, medication dosing, and fetal thyroid surveillance.",
    "decks/obesity-circumvallate/obesity-circumvallate.html":
        "Covers circumvallate placenta and its association with obesity: placental anatomy, risk of abruption, preterm birth, and fetal growth restriction surveillance.",
    "decks/mcda-twins/twin_pregnancy_counseling.html":
        "Covers monochorionic-diamniotic (MCDA) twin pregnancy: twin-to-twin transfusion syndrome (TTTS) surveillance, Quintero staging, fetoscopic laser therapy, and delivery timing.",
    "decks/preterm-birth/preterm-birth.html":
        "Clinical management guide for preterm birth: risk stratification, cervical length screening, progesterone therapy, tocolysis, antenatal corticosteroids, and delivery planning.",
    "decks/hypertensive-disorders-doctors/hypertensive_disorders_pregnancy.html":
        "Comprehensive clinical guide to classifying and managing gestational hypertension, preeclampsia, eclampsia, and HELLP syndrome per ACOG guidelines.",
    "decks/fetal-neuroradiology/fetal-neuroradiology.html":
        "Clinical overview of fetal brain imaging: ventriculomegaly, corpus callosum agenesis, posterior fossa abnormalities, and the role of fetal MRI in neuroradiology.",
    "decks/fgr-ua-aedv-35w/index.html":
        "Addresses the management of fetal growth restriction with absent end-diastolic flow at 35 weeks, including Doppler interpretation, corticosteroids, and delivery decision-making.",
    "decks/iugr-and-doppler/IUGR and Abnormal Doppler.html":
        "Clinical overview of intrauterine growth restriction and Doppler velocimetry, covering umbilical artery, MCA, and ductus venosus waveform interpretation for fetal surveillance.",
    "decks/preeclampsia/preeclampsia-expanded.html":
        "Explore evidence-based strategies for preeclampsia diagnosis and management. Covers blood pressure thresholds, magnesium sulfate, delivery timing, and postpartum care.",
    "decks/patient education-sga/pregnancy_education_slideshow.html":
        "Covers the distinction between constitutional SGA and pathologic FGR, surveillance protocols, growth scan intervals, and delivery timing for small-for-gestational-age fetuses.",
    "decks/ama-ptd/ama-ptd.html":
        "Explores the association between advanced maternal age and preterm delivery risk, including proposed mechanisms, cervical length screening, and progesterone prophylaxis.",
    "decks/cervical-incompetence-cerclage/cervical_incompetence_cerclage_presentation.html":
        "Explains cervical insufficiency: diagnosis by history and ultrasound, McDonald and Shirodkar cerclage techniques, progesterone therapy, and cervical length surveillance.",
    "decks/factor-v-leiden/factor_v_leiden_pregnancy_presentation.html":
        "Explains Factor V Leiden thrombophilia in pregnancy: VTE risk stratification, anticoagulation indications, LMWH dosing, and postpartum thromboprophylaxis guidance.",
    "decks/preconception-counseling/preconception_counseling_guide.html":
        "Comprehensive preconception guide: folic acid supplementation, medication review, chronic disease optimization, genetic carrier screening, and lifestyle modifications before pregnancy.",
    "decks/pprom-doctors/index.html":
        "Covers preterm premature rupture of membranes (PPROM): diagnosis with ferning and pooling, latency antibiotics, corticosteroids, GBS prophylaxis, and delivery timing.",
    "decks/jacobs-syndrome-XYY/jacobs-syndrome-XYY.html":
        "Patient-friendly explanation of 47,XYY (Jacobs syndrome): physical and developmental features, fertility implications, and the spectrum of outcomes for affected individuals.",
    "decks/alpha-thallasemia/alpha-thalassemia.html":
        "Explains alpha thalassemia trait: gene deletion patterns, MCV/MCB findings, partner testing, and the risk of Hb Bart's hydrops fetalis when both partners are carriers.",
    "decks/sickle-cell-carrier-status/sickle-cell-carrier-status.html":
        "Covers sickle cell trait: inheritance pattern, partner testing, risk of sickle cell disease in offspring, and reproductive counseling for carriers.",
    "decks/twins-delivery-timing/twins-delivery-timing.html":
        "Evidence-based guide to delivery timing for twin pregnancies by chorionicity: Di-Di at 38 weeks, MCDA at 36\u201337 weeks, and MCMA at 32\u201334 weeks per ACOG guidelines.",
    "decks/syphilis-in-pregnancy/syphilis-in-pregnancy.html":
        "Covers syphilis screening in pregnancy: RPR/VDRL testing, staging, penicillin treatment, Jarisch-Herxheimer reaction, and prevention of congenital syphilis.",
    "decks/menopausal-therapy/menopausal_therapy_onyeije.html":
        "Covers menopausal hormone therapy (MHT): estrogen and progesterone options, benefits for vasomotor symptoms and bone density, cardiovascular risk, and breast cancer considerations.",
    "decks/screening-lifespan-n-onyeije/screening_lifespan_onyeije.html":
        "Comprehensive women's health screening guide: Pap smears, mammography, DEXA, colorectal cancer screening, and age-specific preventive care from adolescence through menopause.",
    "decks/choroid-plexus-cyst/choroid_plexus_cyst_patient_education.html":
        "Explains choroid plexus cysts (CPCs) found on second-trimester ultrasound: their association with trisomy 18, isolated vs. associated findings, and management guidance.",
    "decks/single-umbilical-artery/single_umbilical_artery.html":
        "Covers single umbilical artery (two-vessel cord): association with fetal anomalies and FGR, recommended workup, growth scan surveillance, and delivery planning.",
    "decks/unity-fetal-antigen/unity_fetal_antigen_slides.html":
        "Covers UNITY fetal antigen testing for red cell alloimmunization risk: how cell-free fetal DNA determines fetal antigen status to guide anti-D prophylaxis decisions.",
    "decks/vein-of-galen-malformation/vein_of_galen_malformation%20%281%29.html":
        "Explains vein of Galen malformation: arteriovenous shunting, high-output cardiac failure, ultrasound and MRI diagnosis, neonatal management, and neurodevelopmental prognosis.",
    "decks/fetal-kick-count-slides/fetal_kick_counting_slides.html":
        "Teaches the Cardiff Count-to-Ten method for fetal kick counting: normal movement patterns, how to track kicks, and when to contact a provider for decreased fetal movement.",
}


def main():
    with open(JSON_PATH, "r", encoding="utf-8") as fh:
        data = json.load(fh)

    updated = 0
    for p in data["presentations"]:
        href = p["href"]
        if href in DESCRIPTIONS and not p.get("description"):
            p["description"] = DESCRIPTIONS[href]
            updated += 1

    with open(JSON_PATH, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    print(f"Updated {updated} entries with curated descriptions.")
    missing = [p["href"] for p in data["presentations"] if not p.get("description")]
    if missing:
        print(f"Still missing descriptions: {missing}")
    else:
        print("All 83 presentations now have descriptions.")


if __name__ == "__main__":
    main()
