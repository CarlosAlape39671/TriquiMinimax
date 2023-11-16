from nodos.tableroNode import TableroNode

class TableroNodeRoot:
    
    def __init__(self, new_root_data = None, new_root_score = None):
        if new_root_data:
            self.root_node = TableroNode(new_root_data, new_root_score)
        else:
            self.root_node = None    