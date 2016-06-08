# Copyright 2016 Mario Graff (https://github.com/mgraffg)

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import argparse
from b4msa.classifier import SVC
# from b4msa.params import ParameterSelection


class CommandLine(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='b4msa')
        self.training_set()
        self.predict_kfold()
        self.param_set()

    def predict_kfold(self):
        pa = self.parser.add_argument
        pa('-k', '--kfolds', dest='n_folds',
           help='Predict the training set using stratified k-fold',
           type=int)

    def training_set(self):
        cdn = 'File containing the training set on csv.'
        self.parser.add_argument('training_set',
                                 nargs='?',
                                 default=None,
                                 help=cdn)

    def param_set(self):
        str = 'No. of parameter combinations for the text model'
        pa = self.parser.add_argument
        pa('-N', '--nparams', dest='n_params', help=str, type=int)

    def main(self):
        self.data = self.parser.parse_args()
        if self.data.n_folds is not None:
            hy = SVC.predict_kfold(self.data.training_set,
                                   n_folds=self.data.n_folds)
            print(hy)

        elif self.data.n_folds is not None and self.data.n_params is not None:
            hy = SVC.predict_kfold_params(self.data.training_set,
                                          n_fold=self.data.n_folds,
                                          n_params=self.data.n_params)


def main():
    c = CommandLine()
    c.main()
    