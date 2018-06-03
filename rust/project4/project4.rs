// Project Euler -- project4.rs

fn is_palindrome(candidate: &str) -> bool {
	candidate == candidate.chars().rev().collect::<String>()
}

fn main() {

	let mut res = Vec::new();
	for i in 100..999 {
		for j in 100..999 {
			let c = i * j;
			if is_palindrome(&(c.to_string())) { res.push(c); }
		}
	}

	println!("{}", res.iter().max().unwrap());

}
