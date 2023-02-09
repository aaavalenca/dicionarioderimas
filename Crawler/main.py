from multiprocessing import Pool
import spider

letter = [
        "a", "b", "c", "d", "e", "e", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
        ] 
       

def main():
    # for i in  letter:
        # print("http://www.portaldalinguaportuguesa.org/index.php?action=fonetica&region=rjo&act=list&letter=" + i)
    pool = Pool(7)
    
    pool.map(spider.bfs,letter)
    pool.close()
    pool.join()
    # letter = "x"
    # spider.bfs(link, suffix + letter, lette r)

if __name__ == '__main__':
    main()

