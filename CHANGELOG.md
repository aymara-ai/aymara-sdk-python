# Changelog

## 1.2.0 (2025-12-04)

Full Changelog: [v1.1.1...v1.2.0](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.1.1...v1.2.0)

### Features

* **api:** api update ([17125fc](https://github.com/aymara-ai/aymara-sdk-python/commit/17125fcc74688dd68333f18023062aabcb170105))
* **api:** api update ([220cdd0](https://github.com/aymara-ai/aymara-sdk-python/commit/220cdd08f961d4baa7366ca976176fbc3a0387c5))
* **api:** api update ([fd69c39](https://github.com/aymara-ai/aymara-sdk-python/commit/fd69c39607aa4417ab48aa527880b2d3569c368a))
* **api:** api update ([7ad63fe](https://github.com/aymara-ai/aymara-sdk-python/commit/7ad63fedcc40615e48d868b9dcbaf6009ad187b3))
* **api:** api update ([b33fe8c](https://github.com/aymara-ai/aymara-sdk-python/commit/b33fe8cdec61db16e899e84a612df8b47f2d299f))
* **api:** api update ([1cb47dd](https://github.com/aymara-ai/aymara-sdk-python/commit/1cb47dd19c2852cec9f128cddcf89e90c38ff4b8))
* **api:** api update ([c6cd478](https://github.com/aymara-ai/aymara-sdk-python/commit/c6cd4782343b1c3f8cc62cf4ecc0ba51caa2272a))
* **api:** api update ([b228992](https://github.com/aymara-ai/aymara-sdk-python/commit/b228992af44ee917d433d2f127f4fe6608f74855))
* **api:** api update ([d9dcf88](https://github.com/aymara-ai/aymara-sdk-python/commit/d9dcf883479a35f70caa26a281042b8c5ef096fc))
* **api:** api update ([b53007b](https://github.com/aymara-ai/aymara-sdk-python/commit/b53007bf7e05476212b7383b8bdb359b07024e3e))
* **api:** api update ([eaca15e](https://github.com/aymara-ai/aymara-sdk-python/commit/eaca15e928d2a5c68d227c0e9190d652c1cd534d))
* **api:** api update ([7dfc056](https://github.com/aymara-ai/aymara-sdk-python/commit/7dfc056c8ed52c2a0df33f3a649615fd349863e9))
* **api:** api update ([324c123](https://github.com/aymara-ai/aymara-sdk-python/commit/324c1235afdef70e76794cfad4b91b0784e011ea))
* **api:** api update ([f125418](https://github.com/aymara-ai/aymara-sdk-python/commit/f1254187576e5af08c8dce9d12d07810eb63b405))
* **api:** api update ([c45076c](https://github.com/aymara-ai/aymara-sdk-python/commit/c45076c0ad8cb0669c2b8ace04733633b8dbc923))
* **api:** api update ([f4822b3](https://github.com/aymara-ai/aymara-sdk-python/commit/f4822b36bdfb60fb40c14ef3ef64b439c44775b5))
* **api:** api update ([5c69913](https://github.com/aymara-ai/aymara-sdk-python/commit/5c69913800003a23fe2f058232799f5ebb8fd883))


### Bug Fixes

* **client:** close streams without requiring full consumption ([35363e9](https://github.com/aymara-ai/aymara-sdk-python/commit/35363e901fa9f057bf8ad2f8beed728bf490bbd6))
* **client:** close streams without requiring full consumption ([7bd6108](https://github.com/aymara-ai/aymara-sdk-python/commit/7bd6108ec0e5291cba877750dce365fed235a7b5))
* compat with Python 3.14 ([115b25a](https://github.com/aymara-ai/aymara-sdk-python/commit/115b25acbb3f57cf1596aa4fce76658759e26bf1))
* compat with Python 3.14 ([4c70ed2](https://github.com/aymara-ai/aymara-sdk-python/commit/4c70ed268e7674afd1a1827e20838decd71e1990))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([92bf3d7](https://github.com/aymara-ai/aymara-sdk-python/commit/92bf3d7ff27e645e31b737101719695f49638eb9))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([c316efa](https://github.com/aymara-ai/aymara-sdk-python/commit/c316efa916d9951a80847882b5476434e3e45f96))
* ensure streams are always closed ([1e240df](https://github.com/aymara-ai/aymara-sdk-python/commit/1e240df7e11f3efc71ded5c356cc9c601536e4ea))
* ensure streams are always closed ([63f71ad](https://github.com/aymara-ai/aymara-sdk-python/commit/63f71ad58e9a4e23836e9857d4966f7bc4a3c44d))


### Chores

* add Python 3.14 classifier and testing ([6566bb7](https://github.com/aymara-ai/aymara-sdk-python/commit/6566bb77ccbdcdb284a833cec7d2adcff26c420f))
* add Python 3.14 classifier and testing ([5129930](https://github.com/aymara-ai/aymara-sdk-python/commit/51299301d14a1e7eed69c285fefa24d414e2f5b0))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([6ebf8a1](https://github.com/aymara-ai/aymara-sdk-python/commit/6ebf8a18b441aed674855c01b5ed7347362d188e))
* **docs:** use environment variables for authentication in code snippets ([bcb0dd1](https://github.com/aymara-ai/aymara-sdk-python/commit/bcb0dd10d2fd06c9ed401de620d07e64601cd5dd))
* **internal/tests:** avoid race condition with implicit client cleanup ([b2238f8](https://github.com/aymara-ai/aymara-sdk-python/commit/b2238f875d2e70863ca5b26eeea38ab9863e9d4b))
* **internal/tests:** avoid race condition with implicit client cleanup ([d3f0703](https://github.com/aymara-ai/aymara-sdk-python/commit/d3f070303559ef82805f5cad15ff794fb4a17f22))
* **internal:** grammar fix (it's -&gt; its) ([4cf564e](https://github.com/aymara-ai/aymara-sdk-python/commit/4cf564ee1ba3c0edf6604695a8272cb78423e0c3))
* **internal:** grammar fix (it's -&gt; its) ([6781a0a](https://github.com/aymara-ai/aymara-sdk-python/commit/6781a0a5da9b85d23abf5ddcca54655216223955))
* **internal:** version bump ([e713339](https://github.com/aymara-ai/aymara-sdk-python/commit/e713339798b913f024577669f1d7cfa66ca4aa42))
* **package:** drop Python 3.8 support ([45428d3](https://github.com/aymara-ai/aymara-sdk-python/commit/45428d3ee306dec747e4176fb7d9416055185581))
* **package:** drop Python 3.8 support ([8287a07](https://github.com/aymara-ai/aymara-sdk-python/commit/8287a07a21615e99895823fe8c398c116fadfe83))
* update lockfile ([e4d7114](https://github.com/aymara-ai/aymara-sdk-python/commit/e4d7114ea100c4724a08e147272dd53af699615d))

## 1.1.1 (2025-10-29)

Full Changelog: [v1.1.0...v1.1.1](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.1.0...v1.1.1)

### Bug Fixes

* **examples_utils:** resolve bug preventing sora generations and fix logging visibility ([#34](https://github.com/aymara-ai/aymara-sdk-python/issues/34)) ([80dedbf](https://github.com/aymara-ai/aymara-sdk-python/commit/80dedbfc9d36235ec68cd74ecd09e3f47da8ed03))

## 1.1.0 (2025-10-29)

Full Changelog: [v1.0.3...v1.1.0](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.0.3...v1.1.0)

### Features

* **api:** api update ([2ca0715](https://github.com/aymara-ai/aymara-sdk-python/commit/2ca07153ae47f2fd224fbac8d58ceca70a35bbe5))
* **api:** api update ([29be9f7](https://github.com/aymara-ai/aymara-sdk-python/commit/29be9f79d74bf4c69d51183740e186844dd15a71))
* **api:** api update ([a23c4fa](https://github.com/aymara-ai/aymara-sdk-python/commit/a23c4fad8c01ac136ca3283d4886322fcf7d5672))
* **api:** api update ([b8a6f05](https://github.com/aymara-ai/aymara-sdk-python/commit/b8a6f05b628f00333eb5211ee8a8ee216abd51f7))
* **api:** api update ([3b21ac4](https://github.com/aymara-ai/aymara-sdk-python/commit/3b21ac4f336785519f75b1584572e0ecf8f4d5c9))
* **api:** api update ([f386c39](https://github.com/aymara-ai/aymara-sdk-python/commit/f386c39ed5ab703d9ae7c619241a1aea4793c92d))
* **client:** add follow_redirects request option ([41774ca](https://github.com/aymara-ai/aymara-sdk-python/commit/41774cab90484b0d66c3a87d6b2fc423a05d34f3))
* **client:** add support for aiohttp ([cc6487c](https://github.com/aymara-ai/aymara-sdk-python/commit/cc6487c7269ba50b84f9cecca8b74ed7dc3dfb94))


### Bug Fixes

* **ci:** correct conditional ([10dcc8c](https://github.com/aymara-ai/aymara-sdk-python/commit/10dcc8ca09a4662d5adc07a9199f46b03214c4b1))
* **ci:** release-doctor — report correct token name ([1a905ea](https://github.com/aymara-ai/aymara-sdk-python/commit/1a905ea5d4cdf9298b230621ff3fed52f731693d))
* **client:** correctly parse binary response | stream ([48ba460](https://github.com/aymara-ai/aymara-sdk-python/commit/48ba4602e29776e2c34e0c7f1a37f8b88e863ac1))
* **package:** support direct resource imports ([938dd60](https://github.com/aymara-ai/aymara-sdk-python/commit/938dd60f3c970fd76aec87b7df8bb909b3f12732))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([c5301a5](https://github.com/aymara-ai/aymara-sdk-python/commit/c5301a5780e15d887788f0a32079f1e8fbed4165))
* **utils:** Fix issue with confidences showing up incorrectly for missing confidences. ([7fb32fb](https://github.com/aymara-ai/aymara-sdk-python/commit/7fb32fb0d8ac18acf994c36cae38c5074912a35a))


### Chores

* **ci:** change upload type ([9681bdc](https://github.com/aymara-ai/aymara-sdk-python/commit/9681bdc11663f6a9b3700c15092eada74bdcabe3))
* **ci:** enable for pull requests ([d7e6731](https://github.com/aymara-ai/aymara-sdk-python/commit/d7e67314535b7d2878fe1f0353d1dd94e236d589))
* **ci:** fix installation instructions ([8b37598](https://github.com/aymara-ai/aymara-sdk-python/commit/8b375983e8345ba10ef519cdc6b1da65055ad398))
* **ci:** only run for pushes and fork pull requests ([80611a5](https://github.com/aymara-ai/aymara-sdk-python/commit/80611a5f806dbddcc693cca7eb008f212982757e))
* **ci:** upload sdks to package manager ([a4d60f3](https://github.com/aymara-ai/aymara-sdk-python/commit/a4d60f3dd81f028878a7f74c048e73a09569d6b5))
* **docs:** grammar improvements ([d49a74e](https://github.com/aymara-ai/aymara-sdk-python/commit/d49a74ef636ebabce475f7fc0e8cc505c3c978b7))
* **docs:** remove reference to rye shell ([2cb26d1](https://github.com/aymara-ai/aymara-sdk-python/commit/2cb26d1141daf9781d7a41272e0409e100d0a823))
* **internal:** avoid lint errors in pagination expressions ([5a3c566](https://github.com/aymara-ai/aymara-sdk-python/commit/5a3c5667e9c12a88a3f8ae7167a6402240605c75))
* **internal:** bump pinned h11 dep ([0bf369e](https://github.com/aymara-ai/aymara-sdk-python/commit/0bf369e25a507675875522f39b2e4d43f5436498))
* **internal:** codegen related update ([a98bd9f](https://github.com/aymara-ai/aymara-sdk-python/commit/a98bd9f33ed13ed151e0279c300fd92cc7e9b928))
* **internal:** update conftest.py ([5b7c341](https://github.com/aymara-ai/aymara-sdk-python/commit/5b7c3418581834e07a9dfbeb4b7e4381264b241d))
* **package:** mark python 3.13 as supported ([403512f](https://github.com/aymara-ai/aymara-sdk-python/commit/403512f5f67e5a755abf79a80d4e48d21e80fbf1))
* **readme:** update badges ([fd2895a](https://github.com/aymara-ai/aymara-sdk-python/commit/fd2895ab11c602307e38c3805357a62338012a66))
* **tests:** add tests for httpx client instantiation & proxies ([5aa538f](https://github.com/aymara-ai/aymara-sdk-python/commit/5aa538f111064a8385393fa6f24079cc9f0c0baf))
* **tests:** run tests in parallel ([6d637ae](https://github.com/aymara-ai/aymara-sdk-python/commit/6d637ae0ca057a63a2988a546b8224929f23b9c3))
* **tests:** skip some failing tests on the latest python versions ([7093c76](https://github.com/aymara-ai/aymara-sdk-python/commit/7093c76947eae3091c4050616a6add7309f9d966))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([df9b5d2](https://github.com/aymara-ai/aymara-sdk-python/commit/df9b5d29b2885baedd789968cf395626ae9d15c3))

## 1.0.3 (2025-05-09)

Full Changelog: [v1.1.0-beta.3...v1.0.3](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.1.0-beta.3...v1.0.3)

## 1.1.0-beta.3 (2025-05-09)

Full Changelog: [v1.1.0-beta.2...v1.1.0-beta.3](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.1.0-beta.2...v1.1.0-beta.3)

### Bug Fixes

* missing dep ([c9c75e9](https://github.com/aymara-ai/aymara-sdk-python/commit/c9c75e9ac682a63afa029bc6d2396e214b2ebf66))

## 1.1.0-beta.2 (2025-05-09)

Full Changelog: [v1.1.0-beta.1...v1.1.0-beta.2](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.1.0-beta.1...v1.1.0-beta.2)

### Features

* async progress ([9871d3f](https://github.com/aymara-ai/aymara-sdk-python/commit/9871d3facde9d458b796e31eeae458c8b9857ff2))


### Chores

* async example ([392c5a7](https://github.com/aymara-ai/aymara-sdk-python/commit/392c5a737955a3b2bfa17243726028ae61c53c39))

## 1.1.0-beta.1 (2025-05-09)

Full Changelog: [v1.0.2...v1.1.0-beta.1](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.0.2...v1.1.0-beta.1)

### Features

* jupyter progress bar ([dde2a93](https://github.com/aymara-ai/aymara-sdk-python/commit/dde2a9301b3851b770192e0475429f503841e435))

## 1.0.2 (2025-05-09)

Full Changelog: [v1.0.1...v1.0.2](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.0.1...v1.0.2)

### Bug Fixes

* image none handling ([143b4aa](https://github.com/aymara-ai/aymara-sdk-python/commit/143b4aaa51479659e85d19fcbb90d5e821912889))
* unwrap page responses ([5a0ff29](https://github.com/aymara-ai/aymara-sdk-python/commit/5a0ff290d48a8a04dad8030bbff117661358b1b4))


### Chores

* **internal:** avoid errors for isinstance checks on proxies ([ef5374f](https://github.com/aymara-ai/aymara-sdk-python/commit/ef5374f732376b9f29cf8affc0b2cf122a88ecff))
* lint ([75432ee](https://github.com/aymara-ai/aymara-sdk-python/commit/75432eefeeb666832a9916d1921a0589bccee105))
* lint ([816d315](https://github.com/aymara-ai/aymara-sdk-python/commit/816d3154fb9d383b868092fc52080af412366fc2))

## 1.0.1 (2025-05-08)

Full Changelog: [v1.0.0...v1.0.1](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.0.0...v1.0.1)

### Bug Fixes

* prompt response alignment in df ([3eae5d3](https://github.com/aymara-ai/aymara-sdk-python/commit/3eae5d34540cac3c84276e869a618d5cedc01b1f))

## 1.0.0 (2025-05-08)

Full Changelog: [v1.0.0-alpha.22...v1.0.0](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.0.0-alpha.22...v1.0.0)

## 1.0.0-alpha.22 (2025-05-08)

Full Changelog: [v1.0.0-alpha.21...v1.0.0-alpha.22](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.0.0-alpha.21...v1.0.0-alpha.22)

### Features

* print report by category ([14d2d31](https://github.com/aymara-ai/aymara-sdk-python/commit/14d2d31d689ff48d0aac4b279a1e54c2204d6e18))

## 1.0.0-alpha.21 (2025-05-08)

Full Changelog: [v1.0.0-alpha.20...v1.0.0-alpha.21](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.0.0-alpha.20...v1.0.0-alpha.21)

### Features

* add category graph ([a0e807c](https://github.com/aymara-ai/aymara-sdk-python/commit/a0e807c817950dd30b71d091746875f95ce3b279))

## 1.0.0-alpha.20 (2025-05-08)

Full Changelog: [v1.0.0-alpha.19...v1.0.0-alpha.20](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.0.0-alpha.19...v1.0.0-alpha.20)

### Bug Fixes

* image display ([2ed5aea](https://github.com/aymara-ai/aymara-sdk-python/commit/2ed5aea7ebb233034b956051ea060b7b15a3fd50))
* image handling for non-scored responses ([b018a38](https://github.com/aymara-ai/aymara-sdk-python/commit/b018a380466cdd8dab1dc108160e114bca8f6eaf))
* scored image display ([95f64df](https://github.com/aymara-ai/aymara-sdk-python/commit/95f64df97cb7902a06482785afc5beb7068d7464))


### Chores

* lint ([7795c70](https://github.com/aymara-ai/aymara-sdk-python/commit/7795c7056fcad4aff8e36058b8483219fcfe4a86))

## 1.0.0-alpha.19 (2025-05-07)

Full Changelog: [v1.0.0-alpha.18...v1.0.0-alpha.19](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.0.0-alpha.18...v1.0.0-alpha.19)

### Bug Fixes

* add lib init ([defae5b](https://github.com/aymara-ai/aymara-sdk-python/commit/defae5b92151e795d2945db2e7f659cc5be9f5fe))

## 1.0.0-alpha.18 (2025-05-06)

Full Changelog: [v1.0.0-alpha.17...v1.0.0-alpha.18](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.0.0-alpha.17...v1.0.0-alpha.18)

### Features

* **api:** api update ([74457a7](https://github.com/aymara-ai/aymara-sdk-python/commit/74457a78fcc843a0e2733a2086bffe39c149d22f))

## 1.0.0-alpha.17 (2025-05-05)

Full Changelog: [v1.0.0-alpha.16...v1.0.0-alpha.17](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.0.0-alpha.16...v1.0.0-alpha.17)

### Chores

* examples ([3588a0c](https://github.com/aymara-ai/aymara-sdk-python/commit/3588a0cee9344e0ce102c202c2aeb447d9c1dbea))

## 1.0.0-alpha.16 (2025-05-05)

Full Changelog: [v1.0.0-alpha.15...v1.0.0-alpha.16](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.0.0-alpha.15...v1.0.0-alpha.16)

### Features

* **api:** api update ([0d3b428](https://github.com/aymara-ai/aymara-sdk-python/commit/0d3b428d0b2205d1ef4db1ac52daf9098b938c07))
* make name optional ([918f8d3](https://github.com/aymara-ai/aymara-sdk-python/commit/918f8d336f82047d96ca7ccbebc07d8da4396b1a))


### Bug Fixes

* use name in plots ([c7977f4](https://github.com/aymara-ai/aymara-sdk-python/commit/c7977f4e2554d23976ad230277faf63ed6782b81))

## 1.0.0-alpha.15 (2025-05-05)

Full Changelog: [v1.0.0-alpha.14...v1.0.0-alpha.15](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.0.0-alpha.14...v1.0.0-alpha.15)

### Features

* use remote image paths ([a51c113](https://github.com/aymara-ai/aymara-sdk-python/commit/a51c1132f6e3fdf815999e2ea1ad0396d8e97631))

## 1.0.0-alpha.14 (2025-05-05)

Full Changelog: [v1.0.0-alpha.13...v1.0.0-alpha.14](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.0.0-alpha.13...v1.0.0-alpha.14)

### Features

* **api:** api update ([44120be](https://github.com/aymara-ai/aymara-sdk-python/commit/44120be06463a5a2058dae16fb53ee3c157f36b1))
* **api:** api update ([baaf7a4](https://github.com/aymara-ai/aymara-sdk-python/commit/baaf7a4ecb15c6c2fcb88d901424420bc4d48b11))
* image upload examples ([a78b4c1](https://github.com/aymara-ai/aymara-sdk-python/commit/a78b4c1642a3908a5f6f958a23dba6571245b7e2))


### Chores

* lint ([bc1b752](https://github.com/aymara-ai/aymara-sdk-python/commit/bc1b752fcc009e523c072324be657b273ae91864))

## 1.0.0-alpha.13 (2025-05-02)

Full Changelog: [v1.0.0-alpha.12...v1.0.0-alpha.13](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.0.0-alpha.12...v1.0.0-alpha.13)

### Features

* file upload utils ([2a728da](https://github.com/aymara-ai/aymara-sdk-python/commit/2a728dadbd363952487687a5bbfa21935877fe36))


### Bug Fixes

* image generation ([9a78e78](https://github.com/aymara-ai/aymara-sdk-python/commit/9a78e78fddcd44052e8e3c61d4c68baedda68387))


### Chores

* lint ([53cbfbd](https://github.com/aymara-ai/aymara-sdk-python/commit/53cbfbd1702b4f04a1a778993ec275a28168f98c))
* lint ([2a0caac](https://github.com/aymara-ai/aymara-sdk-python/commit/2a0caac33ecfaf4f6ef64194bc607fc0ec5b8a91))

## 1.0.0-alpha.12 (2025-05-01)

Full Changelog: [v1.0.0-alpha.11...v1.0.0-alpha.12](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.0.0-alpha.11...v1.0.0-alpha.12)

### Features

* handle bytes from model ([a8e3ca5](https://github.com/aymara-ai/aymara-sdk-python/commit/a8e3ca5cdaabe4f2d8f1d983fb8d66b0b81af0bf))

## 1.0.0-alpha.11 (2025-05-01)

Full Changelog: [v1.0.0-alpha.10...v1.0.0-alpha.11](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.0.0-alpha.10...v1.0.0-alpha.11)

### Features

* add prompt category ([b31a58d](https://github.com/aymara-ai/aymara-sdk-python/commit/b31a58d48b78f5c6eb861faee36344c4e726d49b))

## 1.0.0-alpha.10 (2025-05-01)

Full Changelog: [v1.0.0-alpha.9...v1.0.0-alpha.10](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.0.0-alpha.9...v1.0.0-alpha.10)

### Features

* image eval runner example ([fc0be9e](https://github.com/aymara-ai/aymara-sdk-python/commit/fc0be9e3660a6b08f614f087edbedda382c7d04c))


### Bug Fixes

* async call ([8ed887a](https://github.com/aymara-ai/aymara-sdk-python/commit/8ed887a2d1c104407ee181a4aab5c764c5d3e439))
* image content handling ([ff31da0](https://github.com/aymara-ai/aymara-sdk-python/commit/ff31da00b59fe3920ddcffc3a9b29ad57ffee08c))
* image upload handling ([2317a6a](https://github.com/aymara-ai/aymara-sdk-python/commit/2317a6ae508b0ba9cd8e5a4ac9b156c58e99a75c))
* lint ([875077a](https://github.com/aymara-ai/aymara-sdk-python/commit/875077a3ba09aad8b93967a516495a0530d2ba9d))
* response type ([f42329d](https://github.com/aymara-ai/aymara-sdk-python/commit/f42329d56ad02a4234ce20e627e683a247a14650))

## 1.0.0-alpha.9 (2025-05-01)

Full Changelog: [v1.0.0-alpha.8...v1.0.0-alpha.9](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.0.0-alpha.8...v1.0.0-alpha.9)

### Features

* add df util ([cb37ee7](https://github.com/aymara-ai/aymara-sdk-python/commit/cb37ee79816bd031c8ba9c6d442385596dce223f))
* eval runner ([a95b857](https://github.com/aymara-ai/aymara-sdk-python/commit/a95b85769619d6b42cbf71bd57ab3d7689e746cf))


### Bug Fixes

* eval runner waiting ([ae05de0](https://github.com/aymara-ai/aymara-sdk-python/commit/ae05de0d30053070cc1cfc94721e89de6d5fe528))
* example async ([0ab6116](https://github.com/aymara-ai/aymara-sdk-python/commit/0ab61160ede326967a884276f218da6f9a62876f))
* lint ([e634bd1](https://github.com/aymara-ai/aymara-sdk-python/commit/e634bd1fb1f376fe25a68be83361e5e927837484))

## 1.0.0-alpha.8 (2025-04-30)

Full Changelog: [v1.0.0-alpha.7...v1.0.0-alpha.8](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.0.0-alpha.7...v1.0.0-alpha.8)

### Features

* **api:** api update ([e4fdfa1](https://github.com/aymara-ai/aymara-sdk-python/commit/e4fdfa1b080191a10d9073917e4b8c46d5f3746d))
* **api:** api update ([2d5542f](https://github.com/aymara-ai/aymara-sdk-python/commit/2d5542ffc32c073949b3f982750e4496000669f6))
* **api:** api update ([ba1f23f](https://github.com/aymara-ai/aymara-sdk-python/commit/ba1f23f126842dadc4bd3dc00f5fa70b7969df78))
* **api:** api update ([e4e27bf](https://github.com/aymara-ai/aymara-sdk-python/commit/e4e27bf0e679b25c35c3b78c63cec2fc57d2b9a3))
* **api:** api update ([5a16d43](https://github.com/aymara-ai/aymara-sdk-python/commit/5a16d43cb6a7ec0f5cd6f8a0269bf6230d4a92f7))

## 1.0.0-alpha.7 (2025-04-30)

Full Changelog: [v1.0.0-alpha.6...v1.0.0-alpha.7](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.0.0-alpha.6...v1.0.0-alpha.7)

### Features

* **api:** api update ([6481f2a](https://github.com/aymara-ai/aymara-sdk-python/commit/6481f2ac8ee8c8a490474eb99ccfd9a3f86fed03))

## 1.0.0-alpha.6 (2025-04-30)

Full Changelog: [v1.0.0-alpha.5...v1.0.0-alpha.6](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.0.0-alpha.5...v1.0.0-alpha.6)

### Features

* **api:** api update ([93a6df0](https://github.com/aymara-ai/aymara-sdk-python/commit/93a6df0fb0a07a8b2dbfeb046822768b9b901b51))
* **api:** api update ([d5481e6](https://github.com/aymara-ai/aymara-sdk-python/commit/d5481e68d1f8818407e5663fb6b8a11f810d157e))

## 1.0.0-alpha.5 (2025-04-29)

Full Changelog: [v1.0.0-alpha.4...v1.0.0-alpha.5](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.0.0-alpha.4...v1.0.0-alpha.5)

### Features

* **api:** api update ([9bdc13d](https://github.com/aymara-ai/aymara-sdk-python/commit/9bdc13df35cf0c6124e5a8f15ecd00ff7f5477f4))
* **api:** api update ([d4a927c](https://github.com/aymara-ai/aymara-sdk-python/commit/d4a927c78f25a56152c5cd5337728a62188eb533))
* **api:** api update ([abb7cf1](https://github.com/aymara-ai/aymara-sdk-python/commit/abb7cf12d416dbefe0e9204d234e2f342e64b444))
* **api:** api update ([b61b2c3](https://github.com/aymara-ai/aymara-sdk-python/commit/b61b2c3f4bbba09712295b1062195c9e428b39a2))

## 1.0.0-alpha.4 (2025-04-29)

Full Changelog: [v1.0.0-alpha.3...v1.0.0-alpha.4](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.0.0-alpha.3...v1.0.0-alpha.4)

### Features

* **api:** api update ([07eb785](https://github.com/aymara-ai/aymara-sdk-python/commit/07eb7858edc71540bb874de65f1215686ecdf279))


### Chores

* update SDK settings ([b999566](https://github.com/aymara-ai/aymara-sdk-python/commit/b999566985b677f11701902d2f4667cada23882b))

## 1.0.0-alpha.3 (2025-04-28)

Full Changelog: [v1.0.0-alpha.2...v1.0.0-alpha.3](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.0.0-alpha.2...v1.0.0-alpha.3)

### Features

* **api:** api update ([fe302b7](https://github.com/aymara-ai/aymara-sdk-python/commit/fe302b7962c120be2b207c086f11a34b5793c8ad))


### Chores

* update SDK settings ([614efcb](https://github.com/aymara-ai/aymara-sdk-python/commit/614efcb7e7042398e97230b38e24a0285305ceda))

## 1.0.0-alpha.2 (2025-04-28)

Full Changelog: [v1.0.0-alpha.1...v1.0.0-alpha.2](https://github.com/aymara-ai/aymara-sdk-python/compare/v1.0.0-alpha.1...v1.0.0-alpha.2)

### Chores

* update SDK settings ([12ff7e8](https://github.com/aymara-ai/aymara-sdk-python/commit/12ff7e8b41ea881f9db68f2cc9fc8940f4a36baa))

## 1.0.0-alpha.1 (2025-04-28)

Full Changelog: [v0.0.1-alpha.0...v1.0.0-alpha.1](https://github.com/aymara-ai/aymara-sdk-python/compare/v0.0.1-alpha.0...v1.0.0-alpha.1)

### Features

* **api:** api update ([81a7d7a](https://github.com/aymara-ai/aymara-sdk-python/commit/81a7d7af75c0bb1dcdf78274945a97a104e4fda5))
* **api:** api update ([1ef35bd](https://github.com/aymara-ai/aymara-sdk-python/commit/1ef35bdedd36cbec32fe2ef94464fac3ed164d11))
* **api:** api update ([46311f1](https://github.com/aymara-ai/aymara-sdk-python/commit/46311f1980ef30e4d19a8439d5c3a22755717cec))
* **api:** api update ([0be051a](https://github.com/aymara-ai/aymara-sdk-python/commit/0be051a41ee3d73b701987a0bc2177fd6df14094))
* **api:** api update ([120b839](https://github.com/aymara-ai/aymara-sdk-python/commit/120b839aa9245d87e169bb9c388875bf17739899))
* **api:** api update ([39c82c4](https://github.com/aymara-ai/aymara-sdk-python/commit/39c82c4631ea51e812356f60bd3497ec8f2336c3))
* **api:** api update ([82f7081](https://github.com/aymara-ai/aymara-sdk-python/commit/82f7081655685acd85d8f4a19d99d7c4eeb18ba2))
* **api:** api update ([f517886](https://github.com/aymara-ai/aymara-sdk-python/commit/f517886ca62a5c32a78096743fba1dac15caf830))
* **api:** api update ([f8b6d8d](https://github.com/aymara-ai/aymara-sdk-python/commit/f8b6d8dd90be1e4adf6f879613098b9f6dc2b63b))
* **api:** api update ([51c3d86](https://github.com/aymara-ai/aymara-sdk-python/commit/51c3d8648d5e6eaab395ae8c7368623dd410493a))
* **api:** api update ([fb59f23](https://github.com/aymara-ai/aymara-sdk-python/commit/fb59f236e8ad08a6a8f953f7dfc5e2c904c89f54))
* **api:** api update ([b763fcf](https://github.com/aymara-ai/aymara-sdk-python/commit/b763fcfad6a5783caf00e11e4ec415af81db3cf9))
* **api:** api update ([16cdb93](https://github.com/aymara-ai/aymara-sdk-python/commit/16cdb938e3b7be15f9f482291944e2fa86feb56a))
* **api:** api update ([579739f](https://github.com/aymara-ai/aymara-sdk-python/commit/579739f7fa02ae15cc3731665a7c42c75d6ad206))
* **api:** api update ([fba3ee3](https://github.com/aymara-ai/aymara-sdk-python/commit/fba3ee38a77732340fefb5a3c46c0172990ef848))
* **api:** api update ([a29fe26](https://github.com/aymara-ai/aymara-sdk-python/commit/a29fe26f759fd6d011281e42d3717be78ec54e25))
* **api:** api update ([d2c66ff](https://github.com/aymara-ai/aymara-sdk-python/commit/d2c66ff67ec86d120d50dae386049197bc9953de))
* **api:** api update ([7aeff17](https://github.com/aymara-ai/aymara-sdk-python/commit/7aeff17ee6c642ef8520f0eaf6a85e4195be69a0))
* **api:** update via SDK Studio ([55a6335](https://github.com/aymara-ai/aymara-sdk-python/commit/55a63357fbd363358f2ee8a07cef1313179cf0d6))
* **api:** update via SDK Studio ([d4e2a4f](https://github.com/aymara-ai/aymara-sdk-python/commit/d4e2a4f7bfe8c72cd6b5aceef463ce9d7fa35e8f))
* **api:** update via SDK Studio ([c3c15c8](https://github.com/aymara-ai/aymara-sdk-python/commit/c3c15c802f4f33e318a9e2924412622c72a0c417))
* **api:** update via SDK Studio ([1fa6076](https://github.com/aymara-ai/aymara-sdk-python/commit/1fa6076919fc33ca36e2d061d3672880455e25a1))
* **api:** update via SDK Studio ([9a9c3c6](https://github.com/aymara-ai/aymara-sdk-python/commit/9a9c3c6cf2a423aba823a81f0af4b88189aad1df))
* **api:** update via SDK Studio ([f12ae6b](https://github.com/aymara-ai/aymara-sdk-python/commit/f12ae6b53f510aa4870b47e0002f738abd09092f))
* **api:** update via SDK Studio ([f501250](https://github.com/aymara-ai/aymara-sdk-python/commit/f501250704268c51957ac9083cab941249b1cf24))
* **api:** update via SDK Studio ([89f72e9](https://github.com/aymara-ai/aymara-sdk-python/commit/89f72e9fd5516f4200954cea2b472c027fb0dd07))
* **api:** update via SDK Studio ([8a197ef](https://github.com/aymara-ai/aymara-sdk-python/commit/8a197ef51982cf06fa70958407eba28b2a058b68))
* **api:** update via SDK Studio ([61deb40](https://github.com/aymara-ai/aymara-sdk-python/commit/61deb4032d46d69429baf992a53bfb502c64a852))
* **api:** update via SDK Studio ([8d7097a](https://github.com/aymara-ai/aymara-sdk-python/commit/8d7097ac78ca170a476a097294c55ffdfdb9a054))
* **api:** update via SDK Studio ([77b1e5d](https://github.com/aymara-ai/aymara-sdk-python/commit/77b1e5dd594a0bfaf2a3112e2969a6e0daf2752e))
* **api:** update via SDK Studio ([19b4dd5](https://github.com/aymara-ai/aymara-sdk-python/commit/19b4dd54f15b0d80fbb39d1d6b4be8ce633a9536))
* **api:** update via SDK Studio ([5b033f9](https://github.com/aymara-ai/aymara-sdk-python/commit/5b033f996ac3a2c7080988f9dcd0ae0fbb21d07f))
* **api:** update via SDK Studio ([5c2afe6](https://github.com/aymara-ai/aymara-sdk-python/commit/5c2afe613f1e2ad25bb8cea557a260ec48dbf7db))
* **api:** update via SDK Studio ([f6e82c5](https://github.com/aymara-ai/aymara-sdk-python/commit/f6e82c5643b64147647f7ca1f68162b33619dc89))
* **api:** update via SDK Studio ([1b875c4](https://github.com/aymara-ai/aymara-sdk-python/commit/1b875c4fe4683e6b4d40671b9d314b0e91a16f02))
* **api:** update via SDK Studio ([747e790](https://github.com/aymara-ai/aymara-sdk-python/commit/747e7900b5322d089d9b69f6b0feb3892dd7e1bc))
* **api:** update via SDK Studio ([543e63c](https://github.com/aymara-ai/aymara-sdk-python/commit/543e63caf876a027ae531ebe633cba3998d83923))
* **api:** update via SDK Studio ([bb97eaa](https://github.com/aymara-ai/aymara-sdk-python/commit/bb97eaa56f37e051942c01afb03a1457a01b4ed9))
* **api:** update via SDK Studio ([5c25076](https://github.com/aymara-ai/aymara-sdk-python/commit/5c2507658ff9992da23a8c2151b81dbf49702811))
* **api:** update via SDK Studio ([20b257b](https://github.com/aymara-ai/aymara-sdk-python/commit/20b257b66b814fec517ca8b6878194d64acc3807))


### Bug Fixes

* **pydantic v1:** more robust ModelField.annotation check ([0e645fe](https://github.com/aymara-ai/aymara-sdk-python/commit/0e645fe581069db3500c00bfbd9d7c382efb1508))


### Chores

* broadly detect json family of content-type headers ([cddeb4d](https://github.com/aymara-ai/aymara-sdk-python/commit/cddeb4db3b333aaa903fa6d1d421d9a30a865d6e))
* **ci:** add timeout thresholds for CI jobs ([775db24](https://github.com/aymara-ai/aymara-sdk-python/commit/775db24a3612ef10ec0e6a3b21ea4b5d5d4e4649))
* **ci:** only use depot for staging repos ([51bcc2f](https://github.com/aymara-ai/aymara-sdk-python/commit/51bcc2fb535782d0265149f75795cb7a1f51b411))
* go live ([f01dd76](https://github.com/aymara-ai/aymara-sdk-python/commit/f01dd76d40b69748d8611e87e0247b1d0154cfbe))
* **internal:** base client updates ([d8aacce](https://github.com/aymara-ai/aymara-sdk-python/commit/d8aacce70b18b3ec599f5518a217e9008247cbd6))
* **internal:** bump pyright version ([cce57ad](https://github.com/aymara-ai/aymara-sdk-python/commit/cce57ad4b5a59cc0843e0ecc30e2ba61689047c1))
* **internal:** codegen related update ([67c53c2](https://github.com/aymara-ai/aymara-sdk-python/commit/67c53c2d4c6dab2b37447d4fd7db2988498d9856))
* **internal:** fix list file params ([6f39fdb](https://github.com/aymara-ai/aymara-sdk-python/commit/6f39fdb654e074899008fe9ad2d97efff7a90d33))
* **internal:** import reformatting ([63def71](https://github.com/aymara-ai/aymara-sdk-python/commit/63def7179f79b69c6ffd602e2d09e59a0fc28bb2))
* **internal:** refactor retries to not use recursion ([a12ff04](https://github.com/aymara-ai/aymara-sdk-python/commit/a12ff04d481983e624590d1159102b09c0e7061b))
* **internal:** update models test ([cf41ddf](https://github.com/aymara-ai/aymara-sdk-python/commit/cf41ddf7ea07ae2e9210080b18864ad37cd693f0))
* update SDK settings ([2e9bd76](https://github.com/aymara-ai/aymara-sdk-python/commit/2e9bd76216b40b562c79b7bdf3987bd514005ccf))
* update SDK settings ([4194b25](https://github.com/aymara-ai/aymara-sdk-python/commit/4194b256ab01c3eab0b03e7729ba6e8c8d8a92cb))
* update SDK settings ([e5403c9](https://github.com/aymara-ai/aymara-sdk-python/commit/e5403c93dab1ec0d7181272f9c229a16e1215a84))
* update SDK settings ([f59e2c1](https://github.com/aymara-ai/aymara-sdk-python/commit/f59e2c1b34fc73728b0aba6b62880edb96f82a11))
* update SDK settings ([0669b24](https://github.com/aymara-ai/aymara-sdk-python/commit/0669b245471dc268182f22b0510ea63cdb91f5fc))
* update SDK settings ([4573298](https://github.com/aymara-ai/aymara-sdk-python/commit/4573298e5323fa3669738383af471b192efbc018))
