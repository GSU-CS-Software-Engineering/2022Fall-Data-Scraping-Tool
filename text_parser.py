from nltk import sent_tokenize
import regex as re

class Parser():
    # makes usable regex from user-specified patterns
    def makelist(self, raw_list):
        term_list = raw_list.split(',')
        term_list = [s.strip() for s in term_list]
        term_regex = []
        for term in term_list:
            term_regex.append(term.replace('*', '\w*\s*'))
        term_list = [term.replace('*', '\s*\w*\s*') for term in term_list]
        return term_list




    def demo_parser(self):
        with open('demo_amazon.txt', 'r') as file:
            demo_string = file.read().lower()

            # locates the start and finish of item_1
            item_1 = re.search(r'item 1[:.][ \t\s]*business\s{1,2}(?=\D+)(?!\bitem\b)', demo_string)
            demo_string = demo_string[item_1.end():]
            item_2 = re.search(r'item 2[:.][ \t\s]*properties[\t\s]+(?=\D+)\b(?!\bitem\b)', demo_string)
            demo_string = demo_string[:item_2.start()]
            # sample patterns to match
            infrastructure = self.makelist('control* cost*, control* expense*, control* overhead*, minimiz* cost*, minimiz* '
                                      'expense*, minimiz* overhead*, reduce* cost*,  reduce* expense*, reduce* overhead*, '
                                      'cut* cost*, cut* expense*, cut* over head*, decreas* cost*, decreas* expense*, '
                                      'decreas* overhead*, monitor* cost*,  monitor* expense*, monitor* overhead*, '
                                      'sav* cost*, sav* expense*, sav* over head*, cost* control*, cost* minimization*, '
                                      'cost* reduction*, cost* saving*, cost* improvement*, expense* control*, '
                                      'expense* minimization*, expense*  reduction*, expense* saving*, '
                                      'expense* improvement*, overhead* control*, overhead* minimization*, '
                                      'overhead* reduction*, overhead* saving*, overhead*  improvement*')
            strategic_positioning = self.makelist('differenti*, unique*, superior*, premium*, excellen*,  leading edge, '
                                             'upscale, high* price*, high* margin*, high* end*, inelasticity*, '
                                             'cost  leader*, low* pric*, low* cost*, cost advantage*, competitive pric*, '
                                             'aggressive  pric*')
            operations = self.makelist('efficien*, high* yield*, process* improvement*, asset* utilization*, capacity* '
                                  'utilization*, scope*, scale*, breadth*, broad, mass, high* volume*,  large* volume*, '
                                  'econom* of scale, new* product*, quality*, reliab*, durab*.')

            # split into sentences for troubleshooting
            sentences = sent_tokenize(demo_string)
            term_count_dict = {
                "infrastructure": self.getcount(infrastructure, sentences),
                "strategic_positioning": self.getcount(strategic_positioning, sentences),
                "operations": self.getcount(operations, sentences)
            }
            for key, value in term_count_dict.items():
                print(f"{key}: {value}")

    def getcount(self, regex_list, sentences):
        count = 0
        for regex in regex_list:
            for sentence in sentences:
                if len(re.findall(regex, sentence)) != 0:
                    print(re.findall(regex, sentence))
                    count = count + len(re.findall(regex, sentence))
        return count

if __name__ == "__main__":
    parser = Parser()
    parser.demo_parser()
