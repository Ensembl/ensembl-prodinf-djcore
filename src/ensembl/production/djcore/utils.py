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
import collections
import re


def trim_carriage_return(value):
    """
    Remove (and trim) carriage return char from value
    :param value:
    :return: trimmed value
    """
    t = str.maketrans("\n\r", "  ")
    f_value = value.translate(t)
    return re.sub(' +', ' ', f_value)


def flatten(iter_obj):
    result = []
    for el in iter_obj:
        if isinstance(iter_obj, collections.Iterable) and not isinstance(el, str):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result