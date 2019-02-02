from Sastrawize.Stemmer.Filter import TextNormalizer
import multiprocessing
import math
class CachedStemmer(object):
    """description of class"""
    def __init__(self, cache, delegatedStemmer):
        self.cache = cache
        self.delegatedStemmer = delegatedStemmer

    def stem(self, text, thread_count = multiprocessing.cpu_count()):
        normalizedText = TextNormalizer.normalize_text(text)

        words = normalizedText.split(' ')       
        stems = ''
        cpu_count = thread_count
        queues = [multiprocessing.Queue()] * cpu_count
        processes = [multiprocessing.Process(target = executor, args=(self.inv_stem, i, cpu_count, words, queues[i])) for i in range(cpu_count)]
        [process.start() for process in processes]
        for queue in queues:
            stems += ' '.join(queue.get()) + ' '
        [process.join() for process in processes]
        return stems

   
    def get_cache(self):
        return self.cache
    
    def inv_stem(self, word):
            if self.cache.has(word):
                return self.cache.get(word)
            else:
                stem = self.delegatedStemmer.stem(word)
                self.cache.set(word, stem)
                return stem

def executor(func, exe_num, exe_count, inp, out):
     portion = math.ceil(len(inp) / exe_count)
     start = exe_num * portion
     portion = portion if start+portion<len(inp) else len(inp) - start
     i = start
     output = []
     while i < start+portion:
         output.append(func(inp[i]))
         i += 1
     out.put(output)
     return
