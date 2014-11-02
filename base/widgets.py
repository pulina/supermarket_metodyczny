from django.forms import RadioSelect
from django.template import Context, Template


class StarsRateWidget(RadioSelect):
    TEMPLATE = """
    <div class="starRating">
      <div>
        <div>
          <div>
            <div>
              <input id="{{name}}1" type="radio" name="{{name}}" value="1" {% if value == 1 %}checked{% endif %}>
              <label for="{{name}}1"><span>1</span></label>
            </div>
            <input id="{{name}}2" type="radio" name="{{name}}" value="2" {% if value == 2 %}checked{% endif %}>
            <label for="{{name}}2"><span>2</span></label>
          </div>
          <input id="{{name}}3" type="radio" name="{{name}}" value="3" {% if value == 3 %}checked{% endif %}>
          <label for="{{name}}3"><span>3</span></label>
        </div>
        <input id="{{name}}4" type="radio" name="{{name}}" value="4" {% if value == 4 %}checked{% endif %}>
        <label for="{{name}}4"><span>4</span></label>
      </div>
      <input id="{{name}}5" type="radio" name="{{name}}" value="5" {% if value == 5 %}checked{% endif %}>
      <label for="{{name}}5"><span>5</span></label>
    </div>
    """

    def render(self, name, value=None, attrs=None):
        t = Template(StarsRateWidget.TEMPLATE)
        c = Context({'name': name, 'value': value})
        return t.render(c)