---
name: Publish New Version
about: Publish a new version of andrewtools on PyPI and GitHub
title: ''
labels: ''
assignees: andrewt110216

---

- [ ] Update version in pyproject.toml
- [ ] Update CHANGELOG
- [ ] Update dist files: `python3 -m build`
- [ ] Publish to TestPyPI: `twine upload -r testpypi dist/*`
- [ ] Review TestPyPI publication page for any mistakes
- [ ] Download package locally from TestPyPI and test: `pip install andrewtools`
- [ ] Upload to PyPI: `twine upload dist/*`
- [ ] Publish Release on GH
