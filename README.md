```
      ***********       **********     ************    **********      ****    ***          **********     **********
      *************    ************    ************   ************     ****    ***         ***********    ***********
      *************    ************    ************   ************     ****    ***         ***********    ***********
      ***      ****    ***      ***        ****       ***              ****    ***         ***            ****
      ***      ****    ***      ***        ****       ************     ****    ***         ***********    **********
      ***      ****    ***      ***        ****       ************     ****    ***         ***********    ***********
      ***      ****    ***      ***        ****       ************     ****    ***         ***********     **********
      ***      ****    ***      ***        ****       ***              ****    ***         ***                   ****
      *************    ************        ****       ***              ****    ********    ***********    ***********
      *************    ************        ****       ***              ****    ********    ***********    ***********
      ***********       **********         ****       ***              ****     *******     **********    **********
```

<h2>Overview</h2>

Этот репозиторий является хранилищем моих конфигураций для различных программ.

<img src="./img/Screenshot.PNG" alt="img" width="900px">

<h2>Сonfiguration</h2>

- [GNU Emacs](https://github.com/EgorTolbaev/.emacs.d)

- [Qutebrowser](./qutebrowser/README.md)

- [Home Page](./homepage/README.md)

<h2>Installation</h2>

```
git clone https://github.com/EgorTolbaev/dotfiles.git && cd dotfiles/scripts
```

Скрипт [install.sh](./scripts/install.sh) - проверяет установлены ли [qutebrowser](https://github.com/qutebrowser/qutebrowser), [pandoc](https://github.com/jgm/pandoc) и шрифты [Source Code Pro](https://github.com/adobe-fonts/source-code-pro). Если что то отсутствует предложит установить.

**Warning:** для установки я использовал [pacman](https://wiki.manjaro.org/index.php/Pamac) - менеджер пакетов Manjaro's

```
source install.sh
```

Скрипт [setting_configs.sh](./scripts/setting_configs.sh) - склонирует конфигурации и положит в нужные места.

```
source setting_configs.sh
```
