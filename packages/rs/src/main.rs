use glitch_badges::{make_badge, badge_url, BadgeOptions};
use std::{
    env, fs,
    path::PathBuf,
    process,
};

fn print_help() {
    eprintln!(
        r##"glitch-badges — VRIL LABS animated glitch badge generator

USAGE
  glitch-badges <command> [options]

COMMANDS
  custom <VALUE>          Generate a one-off custom badge
    --tag     <TAG>       Left-side label (optional)
    --accent  <HEX>       Accent colour    (default: #1fe8a8)
    --width   <PX>        Badge width      (default: 220)
    --height  <PX>        Badge height     (default: 36)
    --out     <PATH>      Output .svg path (default: <value>.svg)

  url <collection> <slug> [--wide]
                          Print the raw CDN URL for a pre-built badge

  help                    Show this message

EXAMPLES
  glitch-badges custom "POST QUANTUM" --accent "#a78bfa" --tag Security
  glitch-badges url repo security-pq --wide
"##
    );
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        print_help();
        process::exit(1);
    }

    match args[1].as_str() {
        "help" | "--help" | "-h" => {
            print_help();
        }

        "url" => {
            if args.len() < 4 {
                eprintln!("Usage: glitch-badges url <collection> <slug> [--wide]");
                process::exit(1);
            }
            let collection = &args[2];
            let slug       = &args[3];
            let wide       = args.iter().any(|a| a == "--wide");
            println!("{}", badge_url(collection, slug, wide));
        }

        "custom" => {
            if args.len() < 3 {
                eprintln!("Usage: glitch-badges custom <VALUE> [options]");
                process::exit(1);
            }
            let value = args[2].clone();
            let mut tag:    Option<String> = None;
            let mut accent = "#1fe8a8".to_string();
            let mut width:  u32 = 220;
            let mut height: u32 = 36;
            let mut out:    Option<String> = None;

            let mut i = 3usize;
            while i < args.len() {
                match args[i].as_str() {
                    "--tag"    => { i += 1; tag    = args.get(i).cloned(); }
                    "--accent" => { i += 1; accent = args.get(i).cloned().unwrap_or(accent); }
                    "--width"  => { i += 1; width  = args.get(i).and_then(|v| v.parse().ok()).unwrap_or(width); }
                    "--height" => { i += 1; height = args.get(i).and_then(|v| v.parse().ok()).unwrap_or(height); }
                    "--out"    => { i += 1; out    = args.get(i).cloned(); }
                    _ => {}
                }
                i += 1;
            }

            let svg = make_badge(BadgeOptions {
                text: value.clone(),
                accent,
                width,
                height,
                tag,
                ..Default::default()
            });

            let dest: PathBuf = match out {
                Some(p) => PathBuf::from(p),
                None => {
                    let slug = value
                        .to_lowercase()
                        .split_whitespace()
                        .collect::<Vec<_>>()
                        .join("-");
                    PathBuf::from(format!("{slug}.svg"))
                }
            };

            if let Some(parent) = dest.parent() {
                if !parent.as_os_str().is_empty() {
                    fs::create_dir_all(parent).unwrap_or_default();
                }
            }
            fs::write(&dest, svg).expect("Failed to write SVG");
            println!("✓  {}", dest.display());
        }

        cmd => {
            eprintln!("Unknown command: {cmd}\nRun 'glitch-badges help' for usage.");
            process::exit(1);
        }
    }
}
