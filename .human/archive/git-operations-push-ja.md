---

### 8. Pre-Pushドキュメント化

#### 8.1 Issueコメント要件
**MUST** リモートへpushする前にGitHub Issueにコミット履歴を記録する：

1. **コミットサマリーを生成**:
   ```bash
   git log --oneline origin/<branch>..HEAD --pretty=format:"- %h %s"
   ```

2. **Issueへ投稿**:
   ```bash
   # フルパスでgh CLIを使用
   .agent/runtimes/gh_2.40.1_linux_amd64/bin/gh issue comment <issue-number> --body-file <summary-file>
   # または GitHub Web UI から手動で投稿
   ```

3. **コメント投稿を確認**:
   ```bash
   .agent/runtimes/gh_2.40.1_linux_amd64/bin/gh issue view <issue-number>
   ```

#### 8.2 Pushの実行
**MUST** コミットをドキュメント化した後にpushする：
```bash
git push origin <branch-name>
```

#### 8.3 理由
- **トレーサビリティ**: コミットをIssue議論にリンク
- **監査証跡**: 完了した作業の履歴記録を提供
- **コラボレーション**: チームメンバーに進捗を通知
- **移行サポート**: 別のホスティングサービスへ移行する際にコミット履歴を保持

---
