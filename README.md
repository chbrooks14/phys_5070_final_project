# phys_5070_final_project
This project involves a numerical study of the Henon-Heiles Potential in Python.

In this directory:

-- Omelyan_SST_Solver.py (a python module I wrote to implement the Omelyan SST symplectic integration algorithm from tutorial 20 for a 2D classical Hamiltonian system. I use it throughout the project to solve for the trajectory of a particle in a Henon-Heiles potential for a given set of initial conditions. It also defines the total energy for the Henon-Heiles system for a given 2D position and momentum.)

-- Test_SST_Solver.ipynb (a notebook used for testing the ODE solver in the above module. I implement the solver for a 2D harmonic oscillator and run a series of tests to make sure the solver is implemented correctly.)

-- Explore_HH_Potential.ipynb (a notebook used to study the Henon-Heiles Potential and determine what range of initial conditons give rise to bound orbits.)

-- Classifying_Chaotic_Orbits.ipynb (the main result notebook for this project! An implementation of the Smaller Alignment Index (SALI) to calssify a given Henon-Heiles orbit as either ordered or chaotic. I do a narrow search of the parameter space to determine what initial conditions give rise to chaotic behavior.)

-- Plot_Poincare_Sections.ipynb (a supplemental notebook to go along with the classification of chaotic orbits. I implement a common method of visualizing the phase space trajectories of Henon-Heiles orbits. This lets one compare the phase space plots of ordered vs. chaotic trajectories found using the above notebook.)

-- Poincare_Sections.pdf (a pdf file containing images of Poincare sections from the above notebook ran for a long time to get a clearer picture of the Poincare Sections. Included to save time when grading.)

-- References.txt (a text file that lists the papers that I based my calculations on as well as some supplemental internet sources. They describe the SALI method for classifying chaotic orbits and show its applicability to the Henon-Heiles potential.)
