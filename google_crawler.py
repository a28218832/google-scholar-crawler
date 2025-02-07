#!/usr/bin/env python2

import pickle

from Spider import Spider

def main():
    ### The start page's URL
    start_url = 'https://scholar.google.com.tw/scholar?cites=9030490801850315415&as_sdt=2005&sciodt=0,5&hl=zh-TW'

    ### p_key and n
    # p_key = ['wdrc', 'dynamic range compression', 'hearing aid', 'speech',
    #          'noise cancellation', 'noise reduction', 'feedback cancellation',
    #          'sound', 'hearing loss']
    # n_key = ['imagery', 'image', 'visual', 'video', 'optic', 'opto', 'quantum',
    #          'photon']
    p_key = []
    n_key = []
    
    ### Google Scholar Crawler, Class Spider
    myCrawler = Spider(start_url, p_key, n_key, page=5)

    results = myCrawler.crawl()

    with open('result.pickle', 'wb') as f:
        pickle.dump(results, f, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    main()
