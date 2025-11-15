
# Optimization modelling for utility Scale BESS operations

## Project Overview
This project focuses on the optimization of Battery Energy Storage Systems (BESS) co-located with a solar PV plant. The aim is to maximize the revenue from BESS operations in the Spanish electricity arbitrage market. Anothe use case is considered where BESS is integrated into a data center and the aim of the optimization model is to reduce the electricity costs of the data center. The project uses linear optimization models to achieve these goals.

## Case Study: Solar PV Plant in Spain
- **Plant:** Núñez de Balboa solar PV plant in Badajoz, Spain
- **Capacity:** 500 MW
- **Objective:** Maximize revenue by optimizing the operation of the BESS in the electricity spot market.
- **Market:** Spanish electricity arbitrage market with hourly day-ahead prices from OMIE.

## Data Sources
- **Solar PV Generation Data:**
  - 2020: Simulated using the Photovoltaic Geographical Information System (PVGIS)
  - 2023: Simulated using Renewables.ninja
- **Electricity Price Data:**
  - Hourly day-ahead electricity prices (€/MWh) from the Spanish electricity market operator (OMIE)

## Methodology
### Data Processing
- **Data Collected:**
  - Solar power generation data for 2020 and 2023.
  - Hourly electricity prices for the corresponding years.
- **Preprocessing:** The data is processed to handle missing values, smooth fluctuations, and normalize parameters for model input.

### Optimization Model 1: BESS Co-located with Solar PV
- **Objective:** Maximize the revenue of BESS operating in the electricity arbitrage market.
- **Model Type:** Linear optimization with constraints.
- **Technology Stack:** Python, using optimization libraries.
- **Constraints:**
  - BESS is charged exclusively from the solar PV plant.
  - Charging and discharging schedules are based on electricity price variations.
  - BESS operates with a 100% depth of discharge.
- **Outputs:**
  - Hourly charge/discharge schedules.
  - Weekly and monthly profit trends for 2020 and 2023.
  - Profit-to-Cost ratio (P/C) to determine the optimal BESS size.

### Optimization Model 2: Data Center with BESS
- **Objective:** Reduce the electricity costs of a data center by optimizing BESS operations.
- **Data Used:**
  - Weekly load profile for a typical data center.
  - Electricity price data for week 33, 2024, from the ENTSO-E platform.
- **Optimization Approach:**
  - Similar to the co-located BESS model, with additional constraints for data center load management.
  - Optimize electricity consumption and time-of-use tariffs to reduce costs.
- **Outputs:**
  - Annual savings and P/C ratio for BESS sizes ranging from 20 MW to 200 MW with 2-hour storage capacity.
  - Optimal BESS size determined to be between 50 MW and 100 MW.

## Results
### BESS Co-located with Solar PV
- **2020 vs 2023:**
  - The discharge throughput increased 1.5 times, while profit increased by 5-6 times from 2020 to 2023.
  - Higher revenue was observed in 2023 due to increased electricity price volatility.
- **Profit Trends:**
  - Weekly and monthly profits varied significantly based on price differentials.
  - Optimization results demonstrated that BESS sizes around 2-hour storage showed better ROI than 4-hour storage.

### Data Center with BESS
- **Savings:**
  - BESS helped reduce electricity costs by shifting consumption to lower-priced hours.
  - Annual savings saturated as the BESS size increased, while the P/C ratio decreased.
  - Optimal BESS size for the data center was found to be 50-100 MW with a 2-hour storage duration.

## Business Case & Applications
### Co-located BESS with Solar PV
- **Revenue Opportunities:**
  - BESS allows for revenue stacking through energy arbitrage and ancillary services.
  - Shared infrastructure between the solar plant and BESS reduces operational costs.
  
### Data Center with BESS
- **Cost Reduction:**
  - BESS enhances operational resilience, providing uninterrupted power during outages and lowering energy costs through optimized time-of-use tariffs.
- **Environmental Impact:**
  - Reduced reliance on non-renewable energy sources and diesel generators, lowering emissions.

## Conclusion
The integration of BESS in both co-located solar PV plants and data centers offers significant economic and operational benefits. The linear optimization models presented in this project show that optimizing the BESS operation can increase revenue from electricity arbitrage and reduce electricity costs for data centers. The project highlights the potential of BESS in improving grid stability, enhancing renewable energy integration, and reducing operational costs for industrial consumers.

## Future Work
- **Incorporate Real PV Data:** Using real PV output data to enhance the accuracy of the optimization models.
- **Validation with Operational BESS Data:** Validate model outputs with actual operational data from BESS projects.
- **Explore Hybrid PPAs:** Investigate evolving contractual structures between IPPs, BESS operators, and industrial consumers to maximize profits.
- **Load Profile Analysis:** Conduct a more extensive analysis of load patterns in data centers to improve BESS sizing and operational strategies.

## References
- Iberdrola, Núñez de Balboa Photovoltaic Plant [Link](https://www.iberdrola.com/about-us/what-we-do/solar-photovoltaic-energy/nunez-de-balboa-photovoltaic-plant)
- OMIE - Market Operator [Link](https://www.omie.es)
- European Commission - Energy Storage [Link](https://energy.ec.europa.eu)

<a href="https://github.com/aditya-007/BESS_optimization"> BESS_optimization </a> © 2024 by <a href="https://github.com/aditya-007">Aditya</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA 4.0</a><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/sa.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;">
