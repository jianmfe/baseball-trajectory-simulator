# Baseball Trajectory Simulator (Statcast-style)

A high-precision physical and numerical simulator for baseball trajectories, developed in Python. It models the flight path of a batted ball by solving a system of Ordinary Differential Equations (ODEs) using the Runge-Kutta 4th Order (RK4) numerical method, taking into account aerodynamic drag and horizontal wind effects.

## Features
- Statcast Metrics Integration: Inputs based on real-world tracking data (*Exit Velocity* in mph and *Launch Angle* in degrees).
- Advanced Aerodynamics: Computes relative air velocity against drag forces and custom wind conditions (tailwind/headwind).
- Numerical Rigor: Solves 2D motion equations step-by-step using an RK4 solver with precise ground-impact linear interpolation.
- Imperial Conversion: Outputs final distance metrics in standard baseball units (feet).

## Project Structure
- main.py: Core simulation script with interactive console input and RK4 solver.
- test_trajectory.py: Unit tests validating physical boundaries and wind behavior.
- .gitignore: Excludes cache files and local environment configurations.

## Requirements
Standard Python 3.x installation (uses only built-in libraries like math).

## How to Run

1. Run the main simulation script:
   `bash
   python main.py