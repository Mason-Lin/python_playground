from Deck import Deck


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class NotFreecell:
    valid_group = ["c0", "c1", "c2", "c3", "f0", "f1", "f2", "f3", "p0", "p1", "p2", "p3", "p4", "p5", "p6", "p7"]

    def __init__(self, deck: Deck):
        self.piles = [[], [], [], [], [], [], [], []]
        self.cells = [[], [], [], []]
        self.foundations = [[], [], [], []]
        self.mapping = {
            "p": self.piles,
            "c": self.cells,
            "f": self.foundations,
        }

        # init piles
        i = 0
        for card in deck.get_deck():
            self.piles[i].append(card)

            # go to next pile or reset to first piles
            i += 1
            if i == len(self.piles):
                i = 0
        self.print_usage()

    def print_usage(self):
        print("===================================")
        print("Usage: make a move: mv p0 f0 (move from Pile0 to Foundations0)")
        print("       make a move: mv c1 p2 (move from Cell1 to Pile2)")
        print("       exit (exit game)")
        print("       help (show usage)")
        print("===================================")

    def show_status(self):
        # can refine better print
        print("***********************************")
        print("Cells")
        for i, card in enumerate(self.cells):
            print(f"c{i}:{card} ", end="")
        print("")

        print("Foundations")
        for i, card in enumerate(self.foundations):
            if len(card) != 0:
                print(f"f{i}:[{card[-1]}] ", end="")
            else:
                print(f"f{i}:{card} ", end="")
        print("")

        print("Piles")
        for i, card in enumerate(self.piles):
            print(f"p{i}: {card} ")
        print("***********************************")

    def move(self, src, dst):
        """Logic
        1.cell空的話,可以把單張牌移動到cell
        2.如果cell已有排 不能再進去
        3.foundation空的話 可以把A移動進去
        4.foundation有排 只能進更大的下一張 同色
        5.pile空的話,可以進一張
        6.pile有的話,只能在進更小的不同顏色
        7.永遠都只能動最上面的一張牌

        Name:
        group == pile, cells, foundations
        """
        src_type, src_group = self.get_group_by_nickname(src)
        dst_type, dst_group = self.get_group_by_nickname(dst)

        if len(src_group) == 0:
            return False, "[SKIP] source pile is empty"
        src_top_card = src_group[-1]

        if src_type == "f" and dst_type == "p":
            return False, "[SKIP] Cards from the foundations can not be placed back onto a deck pile"

        # logic cell
        if dst_type == "c":
            if len(dst_group) != 0:
                return False, "[SKIP] Only once card at a time can occupy a freee cell pile"

        # logic foundations
        if dst_type == "f":
            if len(dst_group) == 0:
                if src_top_card.card_face != 1:
                    return False, "[SKIP] Only Ace can be placed in an empty foundation pile"
            else:
                dst_top_card = dst_group[-1]
                if src_top_card.card_face - dst_top_card.card_face != 1:
                    return False, "[SKIP] need to follow ascending order"
                if src_top_card.card_suit != dst_top_card.card_suit:
                    return False, "[SKIP] not a appropriate suit"

        # logic Piles
        if dst_type == "p":
            if len(dst_group) != 0:
                dst_top_card = dst_group[-1]
                if src_top_card.card_face > dst_top_card.card_face:
                    return False, "[SKIP] need to follow descending order"
                black_suit = ["S", "C"]
                red_suit = ["H", "D"]
                if (src_top_card.card_suit in black_suit and dst_top_card.card_suit in black_suit) or (
                    src_top_card.card_suit in red_suit and dst_top_card.card_suit in red_suit
                ):
                    return False, "[SKIP] must be a opposite color"

        dst_group.append(src_group.pop())
        return True, "all good"

    def get_group_by_nickname(self, group_nickname):
        """
        in: p3
        out: group_type, self.piles[3]
        """
        group_type, index = group_nickname
        return group_type, self.mapping[group_type][int(index)]

    def is_win(self):
        for p in self.piles:
            if len(p) != 0:
                return False
        for c in self.cells:
            if len(c) != 0:
                return False
        return True


def main():
    test_deck = Deck(1, 13, 4)
    print("input deck")
    test_deck.shuffle()
    test_deck.display_deck()

    game = NotFreecell(test_deck)

    while not game.is_win():
        print("")
        game.show_status()
        command = input("Make your move:")

        if command == "exit":
            print("bye bye")
            return 0

        if command == "help":
            game.print_usage()
            continue

        # if input not three word may fail here
        mv, src, dst = command.split()

        if mv not in ["mv", "move"]:
            print(f"{bcolors.FAIL} Invalid command {mv} {bcolors.ENDC}")
            continue

        if src not in game.valid_group:
            print(f"{bcolors.FAIL} Invalid source {src} {bcolors.ENDC}")
            continue

        if dst not in game.valid_group:
            print(f"{bcolors.FAIL} Invalid destination {dst} {bcolors.ENDC}")
            continue

        result, reason = game.move(src, dst)
        if result:
            print(f"{bcolors.OKCYAN} move {src} to {dst} {bcolors.ENDC}")
        else:
            print(f"{bcolors.FAIL} Warning: {reason}, try again {bcolors.ENDC}")


if __name__ == "__main__":
    main()
