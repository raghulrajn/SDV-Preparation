# SDV-Preparation
Initial preparation for Hackathon preparation

Hello all, I have created this repository to colloborate for our [Hackathon](https://www.eclipse-foundation.events/event/EclipseSDVHackathon/summary) on November 20-23.

## System Requirements
- Ubuntu 22.04
- Python 3.11.10
- C++
- Rust (Optional)

## Knowlege on Eclipse tools
- uProtocol
- Kuksa
- Ankaios
- Autowrx
- ThreadX
- And others

## To run kuksa databroker

```
cd kuksa-databroker
cargo run --bin databroker -- --metadata data/vss-core/vss_release_4.0.json --insecure
```

## To install bluechi
```
git clone https://github.com/eclipse-bluechi/bluechi.git
cd bluechi
meson setup builddir
meson configure -Dwith_selinux=false builddir
meson compile -C builddir
```

## Clone Ankaois tutorial 
```
git init ankaios
cd ankaios
git remote add origin https://github.com/eclipse-ankaios/ankaios.git
git sparse-checkout init --cone
git sparse-checkout set tools/tutorial_fleet_management
git pull origin main
```

## Sample flow
![flow](/src/flow.jpeg)
## Links to find applications
[digital.auto](https://www.digital.auto/use-cases)


