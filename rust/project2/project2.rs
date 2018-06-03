// Project Euler -- project2.rs

fn fib(n: u32) -> u32 {
	match n {
		0 => 1,
		1 => 1,
		_ => fib(n - 1) + fib(n - 2),
	}
}

fn main() {

	let mut flag: bool = true;
	let mut term = 2;
	let mut s = Vec::new();
	let mut result = 0;
	while flag {
		result = fib(term);
		if result >= 4000000 { flag = false; break; }
		if result % 2 == 0 { s.push(result) }
		term += 1;
	}

	println!("{}", s.iter().fold(0u32, |x,y| x + y));

}
