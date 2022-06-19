use std::io::Write;

// const ALPHA: f64 = std::f64::consts::PI / 4.0;
const ALPHA: f64 = 0.0;
const W0: f64 = 1.0;
const MU0: f64 = 1.0;
const EPS0: f64 = 1.0;
const R: f64 = 1.0;
const SIGMA: f64 = 1.0;
const N: u8 = 201;
const M: u8 = 201;
const DTHETA: f64 = std::f64::consts::PI / (N as f64);
const DPHI: f64 = 2.0 * std::f64::consts::PI / (M as f64);
const K: u8 = 41;
const L: f64 = 3.0;
const DX: f64 = 2.0 * L / (K as f64);
const DY: f64 = DX;
const A: f64 = SIGMA * R * R * DTHETA * DPHI / (36.0 * std::f64::consts::PI * EPS0);
const B: f64 = -SIGMA * R * R * DTHETA * DPHI * MU0 / (4.0 * std::f64::consts::PI * 9.0);

struct Vector3 {
    x: f64,
    y: f64,
    z: f64,
}

impl Vector3 {
    fn new(x: f64, y: f64, z: f64) -> Vector3 {
        Vector3 { x, y, z }
    }

    fn add(&self, other: &Vector3) -> Vector3 {
        Vector3 {
            x: self.x + other.x,
            y: self.y + other.y,
            z: self.z + other.z,
        }
    }

    fn subtract(&self, other: &Vector3) -> Vector3 {
        Vector3 {
            x: self.x - other.x,
            y: self.y - other.y,
            z: self.z - other.z,
        }
    }

    fn dot(&self, other: &Vector3) -> f64 {
        self.x * other.x + self.y * other.y + self.z * other.z
    }

    fn cross(&self, other: &Vector3) -> Vector3 {
        Vector3 {
            x: self.y * other.z - self.z * other.y,
            y: self.z * other.x - self.x * other.z,
            z: self.x * other.y - self.y * other.x,
        }
    }

    fn abs(&self) -> f64 {
        self.dot(&self).powf(0.5)
    }

    fn multiply(&self, other: f64) -> Vector3 {
        Vector3 {
            x: self.x * other,
            y: self.y * other,
            z: self.z * other,
        }
    }
}

fn get_r(r: f64, theta: f64, phi: f64) -> Vector3 {
    Vector3::new(
        r * theta.sin() * phi.cos(),
        r * theta.sin() * phi.sin(),
        r * theta.cos(),
    )
}

fn potential_element(a: u8, b: u8, theta: f64, d: &Vector3) -> f64 {
    (a * b) as f64 * theta.sin() / d.abs()
}
fn electric_field_element(a: u8, b: u8, theta: f64, d: &Vector3) -> Vector3 {
    d.multiply((a * b) as f64 * theta.sin() / d.abs().powi(3))
}

fn magnetic_field_element(
    a: u8,
    b: u8,
    r: Vector3,
    r_p: Vector3,
    w: Vector3,
    theta: f64,
    d: &Vector3,
) -> Vector3 {
    (r.subtract(&r_p))
        .cross(&(w.cross(&r_p)))
        .multiply((a * b) as f64 * theta.sin() * d.abs().powi(-3))
}

fn coeff(i: u8, n: u8) -> u8 {
    if i == 0 || i == n {
        1
    } else if i % 2 == 1 {
        4
    } else {
        2
    }
}

fn main() {
    let w_x: f64 = W0 * ALPHA.sin();
    let w_y: f64 = W0 * ALPHA.cos();
    let w_z: f64 = 0.0;
    let mut file = std::fs::File::create("lab6.csv").expect("create failed");
    file.write_all("x,y,V,Ex,Ey,Bx,By\n".as_bytes())
        .expect("write failed");

    let mut x = -L;
    let mut y;
    while x <= L {
        y = -L;
        while y <= L {
            let mut potential = 0.0;
            let mut electric_field = Vector3::new(0.0, 0.0, 0.0);
            let mut magnetic_field = Vector3::new(0.0, 0.0, 0.0);

            for i in 0..N {
                for j in 0..M {
                    let a = coeff(i, N);
                    let b = coeff(j, M);
                    let r = Vector3::new(x, y, 0.0);
                    let theta = (i as f64) * DTHETA;
                    let phi = (j as f64) * DPHI;
                    let r_vec = get_r(R, theta, phi);
                    let d = r.subtract(&r_vec);
                    potential += potential_element(a, b, DTHETA, &d);
                    electric_field = electric_field_element(a, b, DTHETA, &d).add(&electric_field);
                    magnetic_field = magnetic_field_element(
                        a,
                        b,
                        r,
                        r_vec,
                        Vector3::new(w_x, w_y, w_z),
                        theta,
                        &d,
                    )
                    .add(&magnetic_field);
                }
            }
            potential = potential * A;
            electric_field = electric_field.multiply(A);
            magnetic_field = magnetic_field.multiply(B);

            file.write_all(
                format!(
                    "{},{},{},{},{},{},{}\n",
                    x,
                    y,
                    potential,
                    electric_field.x,
                    electric_field.y,
                    magnetic_field.x,
                    magnetic_field.y
                )
                .as_bytes(),
            )
            .expect("write failed");
            y += DY;
        }
        x += DX;
    }
}
