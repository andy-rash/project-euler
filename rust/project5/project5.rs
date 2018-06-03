// Project Euler -- project5.rs

fn main() {

	let mut idx: u64 = 20;
	let end: u64 = 1_000_000_000;
	while idx < end {

		let mut flag: bool = false;

		for item in &[3,6,7,8,9,11,12,13,14,15,16,17,18,19] {
			if idx % item > 0 {
				flag = true;
				break;
			}
		}

		if flag == false {
			println!("{}", idx);
			break;
		}

		idx += 20;
	}

}
