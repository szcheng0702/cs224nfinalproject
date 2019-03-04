from tensor2tensor.utils.trainer_lib import create_run_config, create_experiment

# Initi Run COnfig for Model Training
RUN_CONFIG = create_run_config(
      model_dir=TRAIN_DIR # Location of where model file is store
      # More Params here in this fucntion for controling how noften to tave checkpoints and more. 
)

# Create Tensorflow Experiment Object
tensorflow_exp_fn = create_experiment(
        run_config=RUN_CONFIG,
        hparams=hparams,
        model_name=MODEL,
        problem_name=PROBLEM,
        data_dir=DATA_DIR, 
        train_steps=400000, # Total number of train steps for all Epochs
        eval_steps=100 # Number of steps to perform for each evaluation
    )

# Kick off Training
tensorflow_exp_fn.train_and_evaluate()
view raw