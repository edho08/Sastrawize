from Sastrawize.Stemmer.Context.Visitor.DontStemShortWord import DontStemShortWord
from Sastrawize.Stemmer.Context.Visitor.RemoveInflectionalParticle import RemoveInflectionalParticle
from Sastrawize.Stemmer.Context.Visitor.RemoveDerivationalSuffix import RemoveDerivationalSuffix
from Sastrawize.Stemmer.Context.Visitor.RemoveInflectionalPossessivePronoun import RemoveInflectionalPossessivePronoun
from Sastrawize.Stemmer.Context.Visitor.PrefixDisambiguator import PrefixDisambiguator
from Sastrawize.Stemmer.Context.Visitor.RemovePlainPrefix import RemovePlainPrefix

from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule1 import DisambiguatorPrefixRule1a, DisambiguatorPrefixRule1b
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule2 import DisambiguatorPrefixRule2
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule3 import DisambiguatorPrefixRule3
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule4 import DisambiguatorPrefixRule4
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule5 import DisambiguatorPrefixRule5
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule6 import DisambiguatorPrefixRule6a, DisambiguatorPrefixRule6b
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule7 import DisambiguatorPrefixRule7
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule8 import DisambiguatorPrefixRule8
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule9 import DisambiguatorPrefixRule9
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule10 import DisambiguatorPrefixRule10
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule11 import DisambiguatorPrefixRule11
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule12 import DisambiguatorPrefixRule12
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule13 import DisambiguatorPrefixRule13a, DisambiguatorPrefixRule13b
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule14 import DisambiguatorPrefixRule14
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule15 import DisambiguatorPrefixRule15a, DisambiguatorPrefixRule15b
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule16 import DisambiguatorPrefixRule16
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule17 import DisambiguatorPrefixRule17a, DisambiguatorPrefixRule17b, DisambiguatorPrefixRule17c, DisambiguatorPrefixRule17d
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule18 import DisambiguatorPrefixRule18a, DisambiguatorPrefixRule18b
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule19 import DisambiguatorPrefixRule19
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule20 import DisambiguatorPrefixRule20
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule21 import DisambiguatorPrefixRule21a, DisambiguatorPrefixRule21b
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule23 import DisambiguatorPrefixRule23
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule24 import DisambiguatorPrefixRule24
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule25 import DisambiguatorPrefixRule25
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule26 import DisambiguatorPrefixRule26a, DisambiguatorPrefixRule26b
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule27 import DisambiguatorPrefixRule27
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule28 import DisambiguatorPrefixRule28a, DisambiguatorPrefixRule28b
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule29 import DisambiguatorPrefixRule29
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule30 import DisambiguatorPrefixRule30a, DisambiguatorPrefixRule30b, DisambiguatorPrefixRule30c
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule31 import DisambiguatorPrefixRule31a, DisambiguatorPrefixRule31b
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule32 import DisambiguatorPrefixRule32
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule34 import DisambiguatorPrefixRule34
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule35 import DisambiguatorPrefixRule35
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule36 import DisambiguatorPrefixRule36
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule37 import DisambiguatorPrefixRule37a, DisambiguatorPrefixRule37b
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule38 import DisambiguatorPrefixRule38a, DisambiguatorPrefixRule38b
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule39 import DisambiguatorPrefixRule39a, DisambiguatorPrefixRule39b
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule40 import DisambiguatorPrefixRule40a, DisambiguatorPrefixRule40b
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule41 import DisambiguatorPrefixRule41
from Sastrawize.Morphology.Disambiguator.DisambiguatorPrefixRule42 import DisambiguatorPrefixRule42

class VisitorProvider(object):
    """description of class"""

    def __init__(self):
        self.visitors = []
        self.suffix_visitors = []
        self.prefix_pisitors = []

        self.init_visitors()

    def init_visitors(self):
        self.visitors.append(DontStemShortWord())

        #{lah|kah|tah|pun}
        self.suffix_visitors.append(RemoveInflectionalParticle())
        #{ku|mu|nya}
        self.suffix_visitors.append(RemoveInflectionalPossessivePronoun())
        #{i|kan|an}
        self.suffix_visitors.append(RemoveDerivationalSuffix())

        #{di|ke|se}
        self.prefix_pisitors.append(RemovePlainPrefix())

        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule1a(), DisambiguatorPrefixRule1b()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule2()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule3()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule4()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule5()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule6a(), DisambiguatorPrefixRule6b()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule7()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule8()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule9()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule10()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule11()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule12()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule13a(), DisambiguatorPrefixRule13b()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule14()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule15a(), DisambiguatorPrefixRule15b()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule16()]))

        disambiguators17 = [DisambiguatorPrefixRule17a(), DisambiguatorPrefixRule17b(), \
            DisambiguatorPrefixRule17c(), DisambiguatorPrefixRule17d()]
        self.prefix_pisitors.append(PrefixDisambiguator(disambiguators17))

        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule18a(), DisambiguatorPrefixRule18b()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule19()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule20()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule21a(), DisambiguatorPrefixRule21b()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule23()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule24()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule25()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule26a(), DisambiguatorPrefixRule26b()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule27()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule28a(), DisambiguatorPrefixRule28b()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule29()]))

        disambiguators30 = [DisambiguatorPrefixRule30a(), DisambiguatorPrefixRule30b(), \
            DisambiguatorPrefixRule30c()]
        self.prefix_pisitors.append(PrefixDisambiguator(disambiguators30))

        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule31a(), DisambiguatorPrefixRule31b()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule32()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule34()]))

        #CS additional rules
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule35()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule36()]))

        #CS infix rules
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule37a(), DisambiguatorPrefixRule37b()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule38a(), DisambiguatorPrefixRule38b()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule39a(), DisambiguatorPrefixRule39b()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule40a(), DisambiguatorPrefixRule40b()]))

        #Sastrawize rules
        #ku-A, kau-A
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule41()]))
        self.prefix_pisitors.append(PrefixDisambiguator([DisambiguatorPrefixRule42()]))

    def get_visitors(self):
        return self.visitors

    def get_suffix_visitors(self):
        return self.suffix_visitors

    def get_prefix_visitors(self):
        return self.prefix_pisitors

