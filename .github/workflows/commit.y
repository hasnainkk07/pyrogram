name: Auto Replace and Commit

on:
  workflow_dispatch: # Trigger manually from GitHub Actions
  push:
    branches:
      - master # Replace with your default branch if different

jobs:
  replace-and-commit:
    runs-on: ubuntu-latest

    steps:
      # Checkout the repository
      - name: Checkout Repository
        uses: actions/checkout@v3

      # Set up Python environment (for replacing text)
      - name: Set Up Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.x

      # Replace "pyrogram" with "hasnainkk"
      - name: Replace Text in Repository
        run: |
          find . -type f -name "*.py" -exec sed -i 's/pyrogram/hasnainkk/g' {} \;

      # Commit and push changes
      - name: Commit and Push Changes
        env:
          GITHUB_TOKEN: ${{ secrets.GX_TOKEN }}
        run: |
          git config --global user.name "hasnainkk07"
          git config --global user.email "hasnaindilshad13@gmail.com"
          git add .
          git commit -m "ㅤㅤ"
          git push
