# Wolt Project — установка Codex

Передавайте всю папку `wolt-project/`, не один SKILL.md. В ней находятся правила, references, assets и scripts. Пакет работает standalone без исходного репозитория.

## Все локальные проекты и чаты

Скопируйте `wolt-project` в `~/.agents/skills/wolt-project/`. Если версия уже установлена, сохраните её вне каталога обнаружения skills перед заменой. Не создавайте `wolt-project/wolt-project/SKILL.md`.

Для одного проекта используйте `<project>/.agents/skills/wolt-project/` вместо personal path. Не устанавливайте дубли одного имени. В некоторых существующих установках используется другой настроенный каталог; проверьте текущий путь, если skill уже виден. [Официальные Codex skill paths](https://learn.chatgpt.com/docs/build-skills).

Откройте новую задачу Codex и отправьте:

```text
$wolt-project Дай 5 коротких идей Wolt Restaurants.
```

Если skill не виден, обновите список skills/перезапустите Codex. В CLI/IDE можно проверить `/skills`. Файлы должны находиться в среде, где работает агент; local installation не переносится автоматически в cloud/remote.

## Managed workspace

Для persistent briefs, idea library, projects и approval history попросите:

```text
Используй wolt-project и создай managed Wolt workspace в /absolute/path/to/Wolt-work.
```

Либо из папки skill выполните:

```bash
python3 scripts/init_workspace.py /absolute/path/to/Wolt-work
```

Initializer не перезаписывает существующие файлы. `--merge` добавляет только отсутствующие файлы в сознательно выбранную непустую папку; это не обновление её существующих templates. Уже существующий Wolt workspace не нужно инициализировать заново. Skill остаётся отдельной personal/project-установкой.

## Использование

После выбора идеи — Client Story EN/RU, минимальный visual reference prompt и полный Seedance EN. RU только краткое описание; ZH по запросу. Один кадр допустим, сетка не обязательна. Изображения обычно создаются в ChatGPT/Gemini из image prompt и реальных вложений. Explicit render и video approval — отдельные gates. Недоступный инструмент не считается подключённым от установки skill.

## Обновление и ZIP

Копия обновляется повторным переносом всей новой папки с сохранением прежней версии. Symlink обновляется с исходником и требует доступности пути. Не храните backup с SKILL.md в каталогах автоматического обнаружения.

Из папки skill можно собрать архив:

```bash
python3 scripts/package_skill.py /absolute/output/directory
```

Команда создаёт ZIP + SHA256. Существующий release не перезаписывается: используйте новый VERSION или --label. Для команды можно явно вложить конкретный brief через `--brief /absolute/path/to/brief --label team-brief-version`; это конфиденциальный пакет, не материал для Git.

В обычном ZIP нет реальных briefs/ideas/projects/private notes. Canonical brand assets включены для внутренней команды; архивные logo images не являются automatic generation refs. Перенос private workspace на другой компьютер выполняется отдельно от установки skill.
