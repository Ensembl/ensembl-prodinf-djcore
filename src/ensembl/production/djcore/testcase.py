# See the NOTICE file distributed with this work for additional information
#   regarding copyright ownership.
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#       http://www.apache.org/licenses/LICENSE-2.0
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
from unittest import  TestCase


class CaseExtension(TestCase):
    _models = tuple()

    @classmethod
    def append_model(cls, model):
        cls._models += (model,)

    def _pre_setup(self):
        super(CaseExtension, self)._pre_setup()
        self._map_models('create_table')

    def _post_teardown(self):
        self._map_models('delete_table')
        super(CaseExtension, self)._post_teardown()

    def _map_models(self, method_name):
        for model in self._models:
            try:
                getattr(model, method_name)()
            except AttributeError:
                raise TypeError("{0} doesn't support table method {1}".format(model, method_name))
