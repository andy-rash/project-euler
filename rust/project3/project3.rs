// Project Euler -- project3.rs

fn prime_factors(mut n: i64) -> Vec<i64> {

	let mut res: Vec<i64> = Vec::new();

	while n % 2 == 0 {
		res.push(n);
		n /= 2;
	}

	let mut idx: i64 = 3;
	let end: i64 = (n as f64).sqrt() as i64 + 1;
	while idx < end {
		while n % idx == 0 {
			res.push(idx);
			n /= idx;
		}

		idx += 2;
	}

	if n > 2 { res.push(n); }

	res

}

fn main() {

	println!("{}", prime_factors(600851475143).iter().max().unwrap());

}
