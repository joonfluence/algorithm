import java.util.HashMap;
import java.util.Scanner;

class BinaryTree {
    private HashMap<Character, Node> tree;

    public BinaryTree() {
        tree = new HashMap<>();
    }

    // 노드 추가
    public void addNode(char parent, char left, char right) {
        tree.put(parent, new Node(parent, left, right));
    }

    // 전위 순회 (Pre-order): 루트 → 왼쪽 → 오른쪽
    public void preOrder(char node) {
        if (node == '.')
            return;
        System.out.print(node); // 루트 출력
        preOrder(tree.get(node).left); // 왼쪽 서브트리
        preOrder(tree.get(node).right); // 오른쪽 서브트리
    }

    // 중위 순회 (In-order): 왼쪽 → 루트 → 오른쪽
    public void inOrder(char node) {
        if (node == '.')
            return;
        inOrder(tree.get(node).left); // 왼쪽 서브트리
        System.out.print(node); // 루트 출력
        inOrder(tree.get(node).right); // 오른쪽 서브트리
    }

    // 후위 순회 (Post-order): 왼쪽 → 오른쪽 → 루트
    public void postOrder(char node) {
        if (node == '.')
            return;
        postOrder(tree.get(node).left); // 왼쪽 서브트리
        postOrder(tree.get(node).right); // 오른쪽 서브트리
        System.out.print(node); // 루트 출력
    }

    // 노드 클래스 정의
    private static class Node {
        char item; // 현재 노드 값
        char left; // 왼쪽 자식 노드
        char right; // 오른쪽 자식 노드

        Node(char item, char left, char right) {
            this.item = item;
            this.left = left;
            this.right = right;
        }
    }
}

public class boj_1991 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt(); // 노드 개수
        scanner.nextLine(); // 개행 처리

        BinaryTree bt = new BinaryTree();

        // 트리 구성
        for (int i = 0; i < n; i++) {
            String[] input = scanner.nextLine().split(" ");
            char parent = input[0].charAt(0);
            char left = input[1].charAt(0);
            char right = input[2].charAt(0);
            bt.addNode(parent, left, right);
        }

        // 순회 결과 출력
        bt.preOrder('A'); // 전위 순회
        System.out.println();
        bt.inOrder('A'); // 중위 순회
        System.out.println();
        bt.postOrder('A'); // 후위 순회
        System.out.println();

        scanner.close();
    }
}
