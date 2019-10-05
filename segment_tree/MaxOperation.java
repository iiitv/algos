public class MaxOperation implements IOperation {
    
    @Override
    public long call(long a, long b) {
        return Math.max(a, b);
    }
}