#!/usr/bin/env python
"""
Enter one line description here.

File:

Copyright 2015 Ankur Sinha
Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import nest

poisson = nest.Create('poisson_generator', 1, {'rate': 100.})

parrot1 = nest.Create('parrot_neuron', 1)
parrot2 = nest.Create('parrot_neuron', 1)
parrot3 = nest.Create('parrot_neuron', 1)
parrot4 = nest.Create('parrot_neuron', 1)
parrot5 = nest.Create('parrot_neuron', 1)
parrot6 = nest.Create('parrot_neuron', 1)
parrot7 = nest.Create('parrot_neuron', 1)
parrot8 = nest.Create('parrot_neuron', 1)
parrot9 = nest.Create('parrot_neuron', 1)
parrot10 = nest.Create('parrot_neuron', 1)

sd1 = nest.Create('spike_detector', params={'to_file': True})
sd2 = nest.Create('spike_detector', params={'to_file': True})
sd3 = nest.Create('spike_detector', params={'to_file': True})
sd4 = nest.Create('spike_detector', params={'to_file': True})
sd5 = nest.Create('spike_detector', params={'to_file': True})
sd6 = nest.Create('spike_detector', params={'to_file': True})
sd7 = nest.Create('spike_detector', params={'to_file': True})
sd8 = nest.Create('spike_detector', params={'to_file': True})
sd9 = nest.Create('spike_detector', params={'to_file': True})
sd10 = nest.Create('spike_detector', params={'to_file': True})

nest.Connect(parrot1, sd1)
nest.Connect(parrot2, sd2)
nest.Connect(parrot3, sd3)
nest.Connect(parrot4, sd4)
nest.Connect(parrot5, sd5)
nest.Connect(parrot6, sd6)
nest.Connect(parrot7, sd7)
nest.Connect(parrot8, sd8)
nest.Connect(parrot9, sd9)
nest.Connect(parrot10, sd10)

nest.Connect(poisson, parrot1)
nest.Connect(poisson, parrot2)
nest.Connect(poisson, parrot3)
nest.Connect(poisson, parrot4)
nest.Connect(poisson, parrot5)
nest.Connect(poisson, parrot6)
nest.Connect(poisson, parrot7)
nest.Connect(poisson, parrot8)
nest.Connect(poisson, parrot9)
nest.Connect(poisson, parrot10)

nest.Simulate(1000)
