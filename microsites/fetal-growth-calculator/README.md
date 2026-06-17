# Fetal Growth Biometry Calculator

## Overview
A comprehensive clinical tool for calculating fetal biometry percentiles, estimated fetal weight (EFW), and Doppler indices with automated interpretation using multiple international growth standards.

## Features
- **Multiple Growth Standards** 
  - INTERGROWTH-21st (2014)
  - Hadlock (1991)
  - WHO (2017)
- **Automated Percentile Calculations** for all biometric parameters
  - Biparietal Diameter (BPD)
  - Head Circumference (HC)
  - Abdominal Circumference (AC)
  - Femur Length (FL)
  - Estimated Fetal Weight (EFW)
- **Hadlock Formula EFW Calculation** with automatic computation from biometry
- **Doppler Indices Interpretation**
  - Umbilical Artery Pulsatility Index (UA-PI)
  - Middle Cerebral Artery Pulsatility Index (MCA-PI)
  - MCA Peak Systolic Velocity (MCA-PSV)
  - Automated abnormal flow detection
- **FGR/SGA/LGA Classification** with clinical recommendations
- **Delivery Timing Guidelines** based on growth restriction severity
- **Color-coded Results** for rapid clinical decision-making
- **Dark Mode** support
- **Print/PDF Export** for documentation

## Clinical Standards
Based on:
- INTERGROWTH-21st Project (Papageorghiou et al. 2014)
- Hadlock et al. 1991 biometry and EFW formulas
- WHO Fetal Growth Charts (Kiserud et al. 2017)
- FMF Doppler reference ranges (Acharya, Ciobanu et al.)
- ACOG Practice Bulletin No. 204: Fetal Growth Restriction
- Society for Maternal-Fetal Medicine guidelines

## Key Capabilities
- Identifies Small for Gestational Age (SGA) - EFW <10th percentile
- Identifies Fetal Growth Restriction (FGR) - EFW <3rd percentile or abnormal Doppler
- Identifies Large for Gestational Age (LGA) - EFW >90th percentile
- Provides context-specific management recommendations
- Interprets umbilical artery flow patterns (AEDF/REDF)
- Calculates CPR (Cerebroplacental Ratio) when both UA-PI and MCA-PI are available
- Anemia screening via MCA-PSV (>1.5 MoM threshold)

## Usage
Open index.html in any modern web browser. No server or dependencies required - it's a standalone HTML file with embedded CSS and JavaScript.

### Input Requirements
- **Minimum**: Gestational age + AC + FL (for EFW calculation)
- **Recommended**: Complete biometry (BPD, HC, AC, FL)
- **Optional**: Doppler studies (UA-PI, MCA-PI, MCA-PSV)

## Target Audience
- Maternal-Fetal Medicine specialists
- Obstetricians
- Radiologists performing obstetric ultrasound
- Sonographers
- Perinatologists
- Medical students and residents

## Disclaimer
This tool is for educational purposes and clinical decision support only. It does NOT provide medical advice, diagnosis, or treatment recommendations. All therapeutic decisions must be discussed with and made by a qualified healthcare provider.

## Created By
[DoctorsWhoCode](https://doctorswhocode.blog/)
