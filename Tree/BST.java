public class BST {
    private class Node {
        private int value;
        private Node left;
        private Node Right;
        private int height;

        public Node(int value, int height) {
            this.value = value;
            this.height = height;
        }

        public Node(int value) {
            this.value = value;
        }

    }

    public BST() {

    }

    private Node root;

    public int GetHeight(Node node) {
        if (node == null) {
            return -1;
        }
        return node.height;
    }

    public boolean IsEmpty() {
        return root == null;
    }

    public void Insert(int value) {
        root=Insert(value,root); //This is the method that will we call from main
    }

    private Node Insert(int value, Node node) {
        if (node == null) { // This method will be hidden from user, and work with
                            //Method OverLoading
            node = new Node(value);
            return node;
        }
        if (value<node.value) {
            node.left=Insert(value, node.left);
        }
        if (value>node.value) {
            node.Right=Insert(value, node.Right);
        }
        node.height = Math.max(GetHeight(node.left), GetHeight(node.Right)) + 1;
        return node;
    }

    public void display() {
        display(this.root, "Root Node: ");
    }

    private void display(Node node, String details) {
        if (node == null) {
            return;
        }
        System.out.println(details + node.value);
        display(node.left, "Left child of " + node.value + " : ");
        display(node.Right, "Right child of " + node.value + " : ");
    }
}
