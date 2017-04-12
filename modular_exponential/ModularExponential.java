class ModularExponential {
	static int modularExponential(int base, int power, int mod) {
		int result = 1;
		base = base % mod;
		while(power > 0) {
			if(power%2==1) // i.e. if power is odd it will return 1 (true), else flase
				result = (result * base) % mod;	
			power = power / 2;
			base = (base * base) % mod;			
		}
		return result;
	}

	public static void main(String[] args) {
		int base = 78;
		int pow = 20;
		int mod = 65;
		System.out.println(modularExponential(base, pow, mod));
	}
}