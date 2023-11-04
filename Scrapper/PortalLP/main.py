from multiprocessing import Pool
import portal_lp

letters = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
        ] 

def main():
    # letters = ["w"]
    pool = Pool(len(letters))
    pool.map(portal_lp.bfs,letters)
    pool.close()
    pool.join()

if __name__ == '__main__':
    main()
