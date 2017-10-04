import java.util.Vector;

/**
* A Java implementation of sleep sort.
* Time Complexity : O(max(input))
* (Will work for integers and not real numbers)
*/
public class SleepSort {
    private static final int DELAY_CONST = 25;

    public static void main(String[] args) {
        int[] data = new int[] { 9, 2, 3, 4, 0 };
        sleepSort(data);
        for (int element : data) {
            System.out.println(element);
        }
    }

    private static void sleepSort(int[] data) {
        if (data.length == 0 || data.length == 0)
            return;
        SorterThread[] sorterThreads = new SorterThread[data.length];
        Vector<Integer> sortedList = new Vector<>();
        for (int i = 0; i < sorterThreads.length; i++) {
            sorterThreads[i] = new SorterThread(data[i], sortedList);
            sorterThreads[i].start();
        }
        while (sortedList.size() != data.length) {
            try {
                Thread.sleep(DELAY_CONST * DELAY_CONST);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        for (int i = 0; i < data.length; i++) {
            data[i] = sortedList.get(i);
        }
    }

    private static class SorterThread extends Thread {
        private int sleepTimer;
        private Vector<Integer> target;

        public SorterThread(int sleepTimer, Vector<Integer> target) {
            this.sleepTimer = sleepTimer * DELAY_CONST;
            this.target = target;
        }

        public void run() {
            try {
                Thread.sleep(sleepTimer);
            } catch (Exception e) {
            }
            target.add(sleepTimer / DELAY_CONST);
        }
    }
}
