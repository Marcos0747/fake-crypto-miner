# ~~~ =================================================================== ~~~ #

#🥀

    ######################################
   #                                    #
  #  Code made with 💝 by Marcos0747  #
 #                                   #
#####################################
                                        #🥀

# ~~~ =================================================================== ~~~ #

try:

    import os
    import time
    import random
    from threading import Thread, Event
    from colorama import Fore, Style, init
    from requests.structures import CaseInsensitiveDict

except ImportError as e:
    print(f"           Error importing module: {e}")
    exit()

GOLD = "\033[38;2;255;215;0m"

# ~~~ =================================================================== ~~~ #

logo = rf"""
                    {Fore.GREEN}                        $$\ $$\            $$\           {Fore.RESET}{Fore.RED}$$\       $$\ $$\ $$\                     {Fore.RESET}
                    {Fore.GREEN}                        $$ |$$ |           $$ |          {Fore.RESET}{Fore.RED}$$ |      \__|$$ |$$ |                    {Fore.RESET}
                    {Fore.GREEN}$$\  $$\  $$\  $$$$$$\  $$ |$$ | $$$$$$\ $$$$$$\         {Fore.RESET}{Fore.RED}$$ |  $$\ $$\ $$ |$$ | $$$$$$\   $$$$$$\  {Fore.RESET}
                    {Fore.GREEN}$$ | $$ | $$ | \____$$\ $$ |$$ |$$  __$$\\_$$  _|        {Fore.RESET}{Fore.RED}$$ | $$  |$$ |$$ |$$ |$$  __$$\ $$  __$$\ {Fore.RESET}
                    {Fore.GREEN}$$ | $$ | $$ | $$$$$$$ |$$ |$$ |$$$$$$$$ | $$ |          {Fore.RESET}{Fore.RED}$$$$$$  / $$ |$$ |$$ |$$$$$$$$ |$$ |  \__|{Fore.RESET}
                    {Fore.GREEN}$$ | $$ | $$ |$$  __$$ |$$ |$$ |$$   ____| $$ |$$\       {Fore.RESET}{Fore.RED}$$  _$$<  $$ |$$ |$$ |$$   ____|$$ |      {Fore.RESET}
                    {Fore.GREEN}\$$$$$\$$$$  |\$$$$$$$ |$$ |$$ |\$$$$$$$\  \$$$$  |      {Fore.RESET}{Fore.RED}$$ | \$$\ $$ |$$ |$$ |\$$$$$$$\ $$ |      {Fore.RESET}
                    {Fore.GREEN} \_____\____/  \_______|\__|\__| \_______|  \____/       {Fore.RESET}{Fore.RED}\__|  \__|\__|\__|\__| \_______|\__|      {Fore.RESET}                             
"""

# ~~~ =================================================================== ~~~ #

ui = rf"""                       
                        {Fore.LIGHTMAGENTA_EX}                                                                          Tnx 4 using ─┐{Fore.RESET}
                        {Fore.LIGHTMAGENTA_EX}┌─ [I] INFO ┌───────────────┐                 ┌───────────────┐                        │{Fore.RESET}
                        {Fore.LIGHTMAGENTA_EX}└─┬─────────┤ Crypto Miners ├─────────────┬───┤     Other     ├────────────────────────┴{Fore.RESET}
                        {Fore.LIGHTMAGENTA_EX}  │         └───────────────┘             │   └───────────────┘                         {Fore.RESET}
                        {Fore.LIGHTMAGENTA_EX}  ├─ [1] {GOLD}BTC  | {GOLD}Bitcoin  {Fore.RESET}                 {Fore.LIGHTMAGENTA_EX}├─ [8] {GOLD}Realistic Miner {Fore.RESET}
                        {Fore.LIGHTMAGENTA_EX}  ├─ [2] {GOLD}ETH  | {GOLD}Etherum  {Fore.RESET}                 {Fore.LIGHTMAGENTA_EX}├─ [9] {GOLD}History         {Fore.RESET}
                        {Fore.LIGHTMAGENTA_EX}  ├─ [3] {GOLD}LTC  | {GOLD}Litecoin {Fore.RESET}                 {Fore.LIGHTMAGENTA_EX}└─ [0] {GOLD}Settings        {Fore.RESET}
                        {Fore.LIGHTMAGENTA_EX}  ├─ [4] {GOLD}SOL  | {GOLD}Solana   {Fore.RESET}
                        {Fore.LIGHTMAGENTA_EX}  ├─ [5] {GOLD}POL  | {GOLD}Polygon  {Fore.RESET}
                        {Fore.LIGHTMAGENTA_EX}  ├─ [6] {GOLD}XRP  | {GOLD}XRP      {Fore.RESET}
                        {Fore.LIGHTMAGENTA_EX}  └─ [7] {GOLD}TRX  | {GOLD}Tron     {Fore.RESET}        
"""

# ~~~ =================================================================== ~~~ #

crypto_map = {
    1: "BTC", 2: "ETH", 3: "LTC", 4: "SOL",
    5: "POL", 6: "XRP", 7: "TRX"
}

# ~~~ =================================================================== ~~~ #

class MiningSimulator:
    def __init__(self):
        self.stop_event = Event()
        self.mining = False
        self.valid_hashes = 0
        self.invalid_hashes = 0
        self.total_hashes = 0
        self.start_time = 0
        self.difficulty = 4  
        self.animation_speed = 0.1
        self.colors = {
            'valid': Fore.GREEN,
            'invalid': Fore.RED,
            'status': Fore.CYAN
        }
        os.makedirs('src', exist_ok=True)

# ~~~ =================================================================== ~~~ #

    def generate_hash(self):
        hash_str = ''.join(random.choices('0123456789abcdef', k=64))
        target = '0' * self.difficulty
        is_valid = hash_str.startswith(target)
        return hash_str, is_valid
    
# ~~~ =================================================================== ~~~ #

    def save_valid_hash(self, hash_str):
        with open('src/hits.txt', 'a', encoding='utf-8') as f:
            f.write(f"{hash_str} - {time.ctime()}\n")

# ~~~ =================================================================== ~~~ #

    def mining_animation(self):
        chars = ['⡿', '⣟', '⣯', '⣷', '⣾', '⣽', '⣻', '⢿']
        i = 0
        while not self.stop_event.is_set():
            status = (
                f"           {self.colors['status']}Mining {self.selected_crypto}: {Fore.YELLOW}[{chars[i % 8]}] "
                f"           {self.colors['valid']}Valid: {self.valid_hashes} "
                f"           {self.colors['invalid']}Invalid: {self.invalid_hashes}"
            )
            print(f"\r{status}", end="")
            i += 1
            time.sleep(self.animation_speed)

# ~~~ =================================================================== ~~~ #

    def start_mining(self, crypto):
        self.selected_crypto = crypto
        self.mining = True
        self.valid_hashes = 0
        self.invalid_hashes = 0
        self.start_time = time.time()
        self.stop_event.clear()
        
        print(f"\n           {self.colors['status']}Starting {crypto} mining simulation...")
        print(f"           {Style.DIM}Difficulty: {'0'*self.difficulty} | Press CTRL+C to stop\n")
        
        animation_thread = Thread(target=self.mining_animation)
        animation_thread.start()
        
        try:
            while not self.stop_event.is_set():
                hash_str, is_valid = self.generate_hash()
                self.total_hashes += 1
                if is_valid:
                    self.valid_hashes += 1
                    color = self.colors['valid'] + Style.BRIGHT
                    self.save_valid_hash(hash_str)
                else:
                    self.invalid_hashes += 1
                    color = self.colors['invalid']
                
                print(f"\r           {color}Hash: {hash_str}  ", end="")
                time.sleep(0.01)
        except KeyboardInterrupt:
            self.stop_mining()

# ~~~ =================================================================== ~~~ #

    def stop_mining(self):
        if self.mining:
            self.stop_event.set()
            self.mining = False
            elapsed_time = time.time() - self.start_time
            
            print(f"\n\n           {Fore.YELLOW}Mining stopped!")
            print(f"           {Fore.YELLOW}Total Hashes: {self.valid_hashes + self.invalid_hashes}")
            print(f"           {Fore.RED}Invalid Hashes: {self.invalid_hashes}")
            print(f"           {Fore.YELLOW}Elapsed Time: {elapsed_time:.2f} seconds")
            print(f"           {Fore.GREEN}Valid Hashes: {self.valid_hashes}")
            print(f"           {Fore.MAGENTA}Approximate {self.selected_crypto} mined: {random.uniform(0.0001, 0.001):.6f}\n")

# ~~~ =================================================================== ~~~ #

    def show_info(self):
        print(f"\n           {Fore.CYAN}~~~ INFORMATION ~~~")
        print(f"           {Fore.YELLOW}Version: 1.0")
        print(f"           {Fore.GREEN}Valid hashes path: src/hits.txt")
        print(f"           {Fore.MAGENTA}Total hashes mined: {self.total_hashes}")
        print(f"           {Fore.CYAN}Current difficulty: {'0'*self.difficulty}{Fore.RESET}\n")

# ~~~ =================================================================== ~~~ #

    def show_history(self):
        if os.path.exists('src/hits.txt'):
            with open('src/hits.txt', 'r', encoding='utf-8') as f:
                lines = f.readlines()
                last_hashes = lines[-5:] if len(lines) >=5 else lines
            print(f"\n           {Fore.CYAN}~~~ LAST VALID HASHES ~~~")
            for hash_line in last_hashes:
                print(f"           {Fore.GREEN}{hash_line.strip()}")
        else:
            print(f"\n           {Fore.RED}No records found.{Fore.RESET}")

# ~~~ =================================================================== ~~~ #

    def enable_realistic_mode(self):
        self.difficulty = 5
        self.animation_speed = 0.05
        self.colors['status'] = Fore.LIGHTRED_EX
        print(f"\n           {Fore.RED}Realistic Mode Activated!")
        print(f"           {Fore.YELLOW}Difficulty increased to 5 zeros")
        print(f"           {Fore.LIGHTRED_EX}Animation speed increased!{Fore.RESET}")

# ~~~ =================================================================== ~~~ #

    def open_settings(self):
        print(f"\n           {Fore.CYAN}~~~ SETTINGS ~~~")
        print(f"           1. Change difficulty (Current: {self.difficulty})")
        print(f"           2. Reset statistics")
        print(f"           3. Go back")
        choice = input(f"\n           Select option: ")
        
        if choice == '1':
            new_diff = input("           New difficulty (3-6): ")
            if new_diff.isdigit() and 3 <= int(new_diff) <= 6:
                self.difficulty = int(new_diff)
                print(f"           {Fore.GREEN}Difficulty updated!")
            else:
                print(f"           {Fore.RED}Invalid value!")
        elif choice == '2':
            self.total_hashes = 0
            print(f"           {Fore.GREEN}Statistics reset!")

# ~~~ =================================================================== ~~~ #

def main():
    print(f"{Fore.BLUE}{logo}")
    print(f"{Fore.WHITE}{ui}")
    
    simulator = MiningSimulator()
    
    while True:
        try:
            choice = input(f"\n           {Fore.CYAN}Select option ( 1-0 / I / Q ): ").strip().upper()
            
            if choice == 'Q':
                if simulator.mining:
                    simulator.stop_mining()
                print(f"\n           {Fore.GREEN}Goodbye!\n")
                break
                
            elif choice == 'I':
                simulator.show_info()
                
            elif choice == '8':
                if simulator.mining:
                    print(f"           {Fore.RED}Stop mining first!")
                else:
                    simulator.enable_realistic_mode()
                    
            elif choice == '9':
                simulator.show_history()
                
            elif choice == '0':
                simulator.open_settings()
                
            elif choice.isdigit():
                choice = int(choice)
                if choice in crypto_map:
                    crypto = crypto_map[choice]
                    simulator.start_mining(crypto)
                else:
                    print(f"           {Fore.RED}Invalid option!")
                    
            else:
                print(f"           {Fore.RED}Invalid input!")

        except KeyboardInterrupt:
            simulator.stop_mining()
            print(f"\n           {Fore.YELLOW}Operation cancelled by user")
            break

# ~~~ =================================================================== ~~~ #

if __name__ == "__main__":
    main()

# ~~~ =================================================================== ~~~ #

#🥀

    ######################################
   #                                    #
  #  Code made with 💝 by Marcos0747  #
 #                                   #
#####################################
                                        #🥀

# ~~~ =================================================================== ~~~ #