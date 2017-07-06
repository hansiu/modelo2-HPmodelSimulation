# modelo2-HPmodelSimulation
Second program for a class in molecular modelling (done in june 2016). It carries out a Monte Carlo simulation with simulated annealing for HP protein model.

HP model simplifies protein sequence to only P and H letters that mean "Polar" and "Hydrophobic".

You can manually input your simplified peptide model (HP model) in main.py script and then run python main.py.
It will carry out a Monte Carlo simulation with simulated annealing where starting temperature is T=1 and finishing one is 0.15, with change in every cycle by -0.05.
For every temperature there are carried out K=10000 steps (accepting or not the allowed conformation).
Simulation starts from a line conformation of peptide.

You can change the input parameters in the simulation.py file.

After the simulation there will be a lot of files generated which are:
* graph representing specific heat per temperature
* graph with mean moment of intertia (gyration radius) per temperature
* histograms of number of contacts for each temperature
* text files with statistics
* best.pdb file with a model for a start conformation and one of conformations with best number of contacs for each temperature

(example in ./1)
