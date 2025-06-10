class RulesOfGame:

    """
        Metoda zwraca true, tylko gdy przejscie z polozenia source na destination w jednym ruchu jest zgodne
        z zasadami gry w szachy.
    """
    def is_correct_move(self, source, destination):
        raise NotImplementedError("Subclasses must implement this method")

class Bishop(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        return abs(source_col - dest_col) == abs(source_row - dest_row) and source != destination

class Knight(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination
        
        col_diff = abs(source_col - dest_col)
        row_diff = abs(source_row - dest_row)
        
        return (col_diff == 2 and row_diff == 1) or (col_diff == 1 and row_diff == 2)

class King(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination
        
        col_diff = abs(source_col - dest_col)
        row_diff = abs(source_row - dest_row)
        
        return col_diff <= 1 and row_diff <= 1 and source != destination

class Queen(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination
        
        col_diff = abs(source_col - dest_col)
        row_diff = abs(source_row - dest_row)
        
        # Ruch po przekątnej (jak goniec) lub w linii prostej (jak wieża)
        diagonal_move = col_diff == row_diff
        straight_move = source_col == dest_col or source_row == dest_row
        
        return (diagonal_move or straight_move) and source != destination

class Rook(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination
        
        # Ruch tylko w pionie lub poziomie
        return (source_col == dest_col or source_row == dest_row) and source != destination

class Pawn(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        if source_col == dest_col:
            return (dest_row - source_row == 1) or (source_row == 2 and dest_row - source_row == 2)
        elif abs(source_col - dest_col) == 1:
            return dest_row - source_row == 1
        return False

# TODO: Prosze dokonczyc implementacje kolejnych figur szachowych: Knight, King, Queen, Rook, Pawn
# TODO: Klasy powinny dziedziczyc RulesOfGame