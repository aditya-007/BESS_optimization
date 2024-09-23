# Modeling battery dispatch behavior

This is a project modeling battery storage and dispatch behavior in the Spanish market. The goal is to understand how the example system might perform, the scale of expected profits, and how those profits might vary across the year.

## Organization
Functions to read data and run the optimization are included in the `src` folder. The optimization and exploration of results are included in the `Dispatch optimization` notebook. The `Price exploration` notebook includes a few figures exploring patterns in hourly electricity price values over the course of 2020 and 2023.

## Project specifications
The goal here is to analyze the revenue generation from a battery storage system that is performing energy arbitrage by participating in the Spanish day ahead electricity market for arbitrage. The algorithm optimizes the operation of BESS on historical electricity prices data. But the algorithm can be modified to look at a 24 hour window of current day ahead prices and output the operating schedule for the next day.

### System Requirements
1. The system optimizes the battery storage dispatch (with an optimization time horizon of at
least 1 day) for the day ahead energy market
  - The battery storage’s State of Energy will be continuous between optimization time
horizon boundaries
2. The system shall accept the following as inputs for the battery storage asset:
  - Max discharge power capacity (MW)
  - Max charge power capacity (MW)
  - Discharge energy capacity (MWh)
  - AC-AC Round-trip efficiency (%)
  - Maximum daily discharged throughput (MWh)
3. The system shall accept the following as inputs for the market revenues:
  - Hourly price (euro/MWh)
  - Output of the solar PV plant as charging input
4. The system shall output the following values about a given battery storage system, for a year’s
worth of data, at an hourly resolution
  - Power output (MW)
  - State of Energy (MWh)
5. The system shall output the following summary values about a given storage system:
  - Total annual revenue generation (euro)
  - Total annual charging cost (euro)
  - Total annual discharged throughput (MWh)
6. The system shall output the following plots
  - A plot that includes both hourly battery dispatch and hourly price for the most
profitable week
  - A plot that shows the total profit for each month

### Assignment
Using python, code a model that meets the Overall System Requirements and uses the following inputs and assumptions:
- Battery storage design inputs:
  - Max power capacity (both charge and discharge) = 50 MW
  - Discharge energy capacity = 200 MWh
  - AC-AC round trip efficiency = 85%
  - Maximum daily discharged throughput (MWh) = 200 MWh
- Market prices inputs
  - 2020 and 2023 Hourly prices
  - Taken from Omie/ENTSO-E website
- Assumptions
  - The battery storage system has 100% depth of discharge capabilities
  - The battery storage system does not experience any degradation during the first
year of operation
  - The battery storage system is a price taker (i.e. receives the price as the market
price)
  - The battery storage system charging cost and discharging revenue should both
be based on the wholesale prices
  - The historical price data can be used directly as a proxy for price forecasts (i.e.
no need to forecast future energy prices)
