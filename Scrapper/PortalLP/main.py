from multiprocessing import Pool
import portal_lp
import manipulate_database as md
import os


letters = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
        ] 

def main():
    relative_path = "Scrapper/PortalLP/DB/Letras"
    os.makedirs(relative_path, exist_ok=True)
    
    # letters = ["w", "z"]
    pool = Pool(len(letters))
    pool.map(portal_lp.bfs, letters)
    pool.close()
    pool.join()

    md.merge_database()

if __name__ == '__main__':
    main()
