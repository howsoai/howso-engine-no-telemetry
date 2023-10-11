# Howso Local No-Telemetry Overlay

This project serves simply to overlay add an "extra" configuration to ensure
telemetry is switched off.

It will inject a file `howso/resources/no-telemetry/howso.yml` that contains
the `client_extra_params` option: `version_check: false`.

The goal is to keep this as thin as possible so that no additional effort is
required on a per-release basis of `howso-engine`.

## License

[License](LICENSE.txt)

## Contributing

[Contributing](CONTRIBUTING.md)
