## This repo contain the Data driven approach for modelling the PMDC (12v - 180 rpm) for control application.
The keypoint in this modelling is 
- Data is logged via IR --Tacheometer
- Data is then analyzed via Python with
     -- annotation
     -- Resampling
     -- Smoothing
- The obtained data, Thus become ready for Parameter Identification.
- Genetic algorithm and TF identifier were used for modeling
- The Matlab is then used for validating the modelled motor with real value of motor captured from logger.
