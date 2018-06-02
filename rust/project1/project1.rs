// Project Euler -- project1.rs

fn main() {

	let s: u32 = (0u32..1000)
		.filter(|x| x % 3 == 0 || x % 5 == 0)
		.fold(0,|x,y| x + y);

	println!("{}", s);

}
