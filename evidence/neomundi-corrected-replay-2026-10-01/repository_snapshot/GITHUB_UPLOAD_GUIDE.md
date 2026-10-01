# GitHub Upload Guide

## Objective

Create a clean, versioned GitHub repository for the NeoMundi × OGS interoperability pilot without publishing unapproved partner wording, brand assets, or private evidence.

## Recommended repository settings

- **Repository name:** `neomundi-ogs-interoperability-pilot`
- **Initial visibility:** `Private`
- **Default branch:** `main`
- **Release-candidate tag:** `v1.1.0-rc.1`
- **Final public tag:** create only after joint sign-off
- **Issues:** disabled initially, or limited to repository collaborators
- **Wiki:** disabled
- **Discussions:** disabled until a public engagement policy exists

The exact description and topics are in `docs/REPOSITORY_METADATA.md`.

## Step 1 — Extract and verify

Unzip the package. The folder you upload is the **inner repository folder** named:

```text
neomundi-ogs-interoperability-pilot
```

Open Terminal, move into that folder, and run:

```bash
python3 scripts/verify_repository.py
```

Do not proceed unless the final line reports `Repository validation: PASS`.

## Step 2 — Create the repository on GitHub

1. Sign in to GitHub.
2. Select **New repository**.
3. Enter `neomundi-ogs-interoperability-pilot`.
4. Set visibility to **Private**.
5. Do **not** initialize it with a README, `.gitignore`, or license; those files already exist locally.
6. Create the repository.

## Step 3A — Upload with GitHub Desktop

This is the simplest route when you do not want to manage authentication tokens in Terminal.

1. Open GitHub Desktop.
2. Select **File → Add Local Repository**.
3. Choose the extracted `neomundi-ogs-interoperability-pilot` folder.
4. If GitHub Desktop says it is not yet a Git repository, select **Create a Repository** using the same folder.
5. Confirm the default branch is `main`.
6. Commit all files with:

```text
Initial release candidate: NeoMundi × OGS interoperability pilot v1.1.0-rc.1
```

7. Select **Publish repository**.
8. Keep **Private repository** selected.
9. Confirm the GitHub repository name and publish.

## Step 3B — Upload from Terminal

From the extracted repository folder:

```bash
git init
git checkout -b main
git add .
git commit -m "Initial release candidate: NeoMundi × OGS interoperability pilot v1.1.0-rc.1"
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/neomundi-ogs-interoperability-pilot.git
git push -u origin main
```

Replace `<YOUR_GITHUB_USERNAME>` with your actual GitHub username. GitHub may open a browser sign-in flow or require an authenticated credential helper. Do not paste access tokens into chat, documents, screenshots, or repository files.

## Step 4 — Configure the repository

Use the values in `docs/REPOSITORY_METADATA.md`:

1. Add the repository description.
2. Add the website field only after selecting the canonical page.
3. Add the listed topics.
4. Confirm the repository remains private.
5. Add Sébastien/NeoMundi as a collaborator for review, if mutually agreed.

## Step 5 — Obtain partner sign-off

Send the private repository link with `extras/NEOMUNDI_APPROVAL_REQUEST.md`.

The following items require explicit confirmation before public release:

- public description of NeoMundi and ControlTower;
- signal-field names and meanings;
- selected example;
- architecture diagram;
- attribution language;
- joint conclusion;
- brand and trademark treatment;
- release date;
- corrected evidence-pack attachment decision;
- commercial contact routing.

Record the result in `docs/APPROVAL_CHECKLIST.md`.

## Step 6 — Create the release-candidate tag

After the private repository is pushed:

```bash
git tag -a v1.1.0-rc.1 -m "NeoMundi × OGS public interoperability pilot release candidate"
git push origin v1.1.0-rc.1
```

Create a GitHub Release from that tag and use `extras/GITHUB_RELEASE_DESCRIPTION.md` as the release body. Mark it as a **pre-release**.

Attach the outer ZIP and its `.sha256` file as release assets. Do not attach the corrected private evidence archive until the publication gate explicitly authorizes it.

## Step 7 — Final public release

Only after every blocking item in `docs/PUBLICATION_GATE.md` is cleared:

1. Replace pending fields in the repository.
2. Rerun `python3 scripts/verify_repository.py`.
3. Commit the approved changes.
4. Create a final semantic version tag, such as `v1.1.0`.
5. Create the final GitHub Release.
6. Change repository visibility from private to public.
7. Add the canonical repository link to Judicator.eu and the LinkedIn article/post.

## What not to upload

- private prompts, policy tables, thresholds, internal DPA content, or proprietary decision logic;
- credentials, API keys, access tokens, customer data, or private correspondence;
- unapproved NeoMundi logos or brand files;
- the private corrected evidence pack unless both parties approve the exact public contents;
- any statement that implies production deployment, independent validation, certification, or regulator approval.
