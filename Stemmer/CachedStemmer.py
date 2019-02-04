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
        cpu_count = thread_count
        manager = multiprocessing.Manager()
        queues = [manager.Queue()] * cpu_count
        processes = [multiprocessing.Process(target = executor, args=(self.inv_stem, i, cpu_count, words, queues[i])) for i in range(cpu_count)]
        [process.start() for process in processes]
        dicts = {}
        for queue in queues:
            arr = queue.get()
            dicts[arr[0]] = arr[1:]
        stems = ''
        for i in range(cpu_count):
            s = ' '.join(dicts[i])
            stems = ' '.join([stems, s])
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
     output = [exe_num]
     while i < start+portion:
         output.append(func(inp[i]))
         i += 1
     out.put(output)
     return
