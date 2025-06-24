# Weather Simulation

This project is a **Weather Simulation** that models how weather changes between different conditions — such as sunny, cloudy, rainy, and snowy — over time. The simulation is based on a Markov Chain model, where the weather transitions from one state to another according to specified probabilities and fixed holding times.

The main goal is to realistically mimic how weather might behave over a sequence of hours, where each state persists for a certain duration before potentially changing to a new state based on random chance influenced by the provided probabilities.

## 📌 Project Overview

- The simulation operates with **four possible weather states**:
  - Sunny
  - Cloudy
  - Rainy
  - Snowy

- At any given hour, the weather is in **one and only one state**.

- Two key factors control the simulation:
  1️⃣ **Holding time**: This defines how long (in hours) the weather stays in its current state before it is allowed to change. Each state has its own fixed holding time.  
  2️⃣ **Transition probabilities**: After the holding time expires, the weather chooses its next state based on a set of probabilities assigned for that current state. These probabilities determine the likelihood of moving to each possible state (including possibly staying in the same state).

- The simulation starts with an initial state (`sunny`) and progresses hour by hour, applying these rules:
  - If the holding time for the current state hasn't been reached, the weather remains the same.
  - Once the holding time is reached, a new state is selected randomly according to the transition probabilities.

- The simulation can run for any number of hours, tracking how often each weather state occurs during that period.

## 🚀 What this project does

- Simulates weather behavior over time using holding times and transition probabilities.
- Automatically calculates how long each state persists.
- Outputs the percentage of time spent in each weather state during the simulation period.

## 🔑 What we need to define to run the simulation

- A list of weather states and their corresponding **holding times** (in hours).
- A set of **transition probabilities** for each state, ensuring that the probabilities for each state's possible transitions sum to 1.
- The number of hours to simulate.

## 💡 Core Idea

The project demonstrates how random processes (like weather changes) can be modeled using a Markov Chain with fixed-duration states. It highlights how both the duration of each state and the likelihood of transitions combine to produce realistic, probabilistic weather patterns over time.
