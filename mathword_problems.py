# import re

# from gutenberg import acquire
# from gutenberg import cleanup

from tensor2tensor.data_generators import problem
from tensor2tensor.data_generators import text_problems
from tensor2tensor.utils import registry

import json



@registry.register_problem
class MathwordProblems(text_problems.Text2TextProblem):
  """Predict next line of poetry from the last line. From Gutenberg texts."""

  @property
  def approx_vocab_size(self):
    return 4000

  @property
  def is_generate_per_split(self):
    # generate_data will shard the data into TRAIN and EVAL for us.
    return False

  @property
  def dataset_splits(self):
    """Splits of data to produce and number of output shards for each."""
    # 10% evaluation data
    return [{
        "split": problem.DatasetSplit.TRAIN,
        "shards": 9,
    }, {
        "split": problem.DatasetSplit.EVAL,
        "shards": 1,
    }]



  def generate_samples(self, data_dir, tmp_dir, dataset_split):
    del data_dir
    del tmp_dir
    del dataset_split

    with open('AllData.json') as j_data:
        data = json.load(j_data)

    q2e={}

    for ex in data:
        if ex.get('sQuestion') and ex.get('lEquations'):
            if len(ex['lEquations'])>1:
                dict_value=' '.join(ex['lEquations'])
            else:
                dict_value=ex['lEquations'][0]
            q2e[ex['sQuestion']]=dict_value


    for que,equ in q2e.items():
      yield {"inputs":que,
            "targets":equ}
      



